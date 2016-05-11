(ns reward-system.handler
  (:require [compojure.core :as cc]
            [compojure.route :as route]
            [ring.middleware.defaults :refer [wrap-defaults site-defaults]]
            [reward-system.views :as views]
            )
  (:use [ring.middleware.params]
        [ring.middleware.multipart-params]
        [ring.adapter.jetty]
        [ring.util.response]
        [clojure.java.io]
        [compojure.handler]
        [reward-system-business.ranking-manager]
        [reward-system-infra.io-manager])
  )

;; Routes for the application
(cc/defroutes app-routes
              ;Index routes
              (cc/GET "/" [] (views/index))
              (cc/GET "/index" [] (views/index))

              ;Ranking routes
              (cc/GET "/upload" [] (views/upload))
              (cc/POST "/upload" {params :params} (let [file (get params "file")]
                                                    (upload-file file)
                                                    )
                       (views/upload-result)
                       )

              ;Invite routes
              (cc/GET "/invite" [] (views/invite))
              (cc/POST "/invite" {params :params}
                       (let [customerid (get params "customer-id")
                             invitee-id (get params "invitee-id")]
                         (add-to-data-file (str "\n" customerid " " invitee-id))
                         )
                       (views/invite-result params)
                       )
              (route/resources "/")
              (route/not-found "Not Found"))

(def app
  (-> app-routes
      wrap-params
      wrap-multipart-params)
  )