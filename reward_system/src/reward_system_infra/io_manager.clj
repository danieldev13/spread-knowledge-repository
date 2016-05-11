(ns reward-system-infra.io-manager
  (:use [clojure.java.io]
        [reward-system-infra.configuration-manager])
  (:import [java.io File])
  )

(defn upload-file [file]

  (let [actual-file (file :tempfile)]
    (do
      (copy actual-file (File. (data-file)))
      )
    )
  )

(defn add-to-data-file [item]
  (with-open [writer (writer (data-file) :append true)]
    (.write writer (str item)))
  )
