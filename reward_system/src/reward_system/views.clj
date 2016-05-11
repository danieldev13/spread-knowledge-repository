(ns reward-system.views
  (:require [hiccup.page :as hpage]
            [clojure.data.json :as json])
  (:use [reward-system-business.ranking-manager :as controller]
        [reward-system-infra.configuration-manager])
  )

(defn show-ranking []
  (try
    (json/read-str (controller/extract-ranking (format (data-file))))
    (catch Exception ex
      (println ex)
      (json/read-str "{ \"data\": []}")
      )
    )

  )

(defn render-head [title]
  [:head
   [:title "Nubak Reward System - " title]
   (hpage/include-css "/css/site.css")
   ])

(def menu
  [:div
   "[ "
   [:a {:href "/index"} "Home"]
   " | "
   [:a {:href "/upload"} "Upload"]
   " | "
   [:a {:href "/invite"} "Invite"]
   " ]"])

(defn render-ranking-grid [ranking-data]
  [:p [:table {:class "rwd-table"}
       [:tr [:th "Customer Id"] [:th "Points"]]
       (for [item (get-in ranking-data ["data"]) ]
         [:tr [:td (get-in item ["inviter"]) ] [:td (get-in item ["points"])]])
       ]
   ]
  )

(defn render-empty-ranking-grid []
  [:p "No data available. Please upload file containing valid data."]
  )

(defn index []
  (hpage/html5
    (render-head "Home")
    menu
    [:h1 "Customer Ranking"]
    (let [ranking-data (show-ranking)]
      (println ranking-data)
      (if (> (count (get-in ranking-data ["data"])) 0)
        (render-ranking-grid ranking-data)
        (render-empty-ranking-grid)
        )
      )
    ))

(defn upload []
  (hpage/html5
    (render-head "Upload")
    menu
    [:h1 "Upload data file"]
    [:form {:action "/upload" :method "POST" :enctype "multipart/form-data"}
     [:p [:label "Data file: "] [:input {:type "file" :name "file" :id "file"  :size 180}] [:input {:type "submit" :name "submit" :value "Send"}]]
     ]))

(defn upload-result []
  (hpage/html5
    (render-head "Ranking File Uploaded")
    menu
    [:h1 "Ranking data uploaded succesfully"]
    (let [ranking-data (show-ranking)]

      (if (> (count (get-in ranking-data ["data"])) 0)
        (render-ranking-grid ranking-data)
        (render-empty-ranking-grid)
        )
      )
    )
  )

(defn invite []
  (hpage/html5
    (render-head "Invite")
    menu
    [:h1 "invite"]
    [:form {:action "/invite" :method "POST" }
     [:p [:label "Customer id: "][:input {:type "text" :name "customer-id" :id "customer-id"}]]
     [:p [:label "Invitee id: "] [:input {:type "text" :name "invitee-id" :id "invitee-id"}]]
     [:p [:input {:type "submit" :value "Invite"}]]
     ]))

(defn invite-result [{:keys [customer-id, invitee-id]}]
  (hpage/html5
    (render-head "Invite Sent")
    menu
    [:h1 "Thanks customer " customer-id ". Invitation sent succesfully to customer " invitee-id]
    (let [ranking-data (show-ranking)]

      (if (> (count (get-in ranking-data ["data"])) 0)
        (render-ranking-grid ranking-data)
        (render-empty-ranking-grid)
        )
      )
    )
  )

