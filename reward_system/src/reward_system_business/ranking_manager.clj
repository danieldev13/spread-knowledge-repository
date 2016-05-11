(ns reward-system-business.ranking-manager
  (:require [clojure.java.io :as io]
            [clojure.string :as string])
  )

(defn extract-data-from-file [file-path]
  (with-open [file-reader (io/reader file-path)]
    (vec (distinct (mapv (fn [line]
                           (mapv #(Integer/parseInt %) (string/split line #"\s+")))
                         (line-seq file-reader))))
    ))

(defn remove-invalid-invitations [original-collection ]
  (first (reduce (fn [[result previous] [a b]]
                   [(if (contains? previous b)
                      result
                      (conj result [a b]))
                    (conj previous b)])
                 [[] #{}]
                 original-collection)))

(defn relationship-first-column [x data]
  (filter #(= (first %) x) data)
  )

(defn relationship-by-level [x data n]
  (vec (when (pos? n)
         (nth (iterate #(mapcat (fn [[_ k]] (relationship-first-column k data)) %)
                       [[nil x]])
              n)))
  )

(defn longer-list [x y]
  (if (> (count x) (count y))
    x
    y)
  )

(defn pad-list [l min-len default-value]
  (into l (take (- min-len (count l)) (repeat default-value)))
  )

(defn merge-list [a b]
  (vec (let [a-len (count a)
             b-len (count b)
             longer-input (if (> a-len b-len)
                            a
                            b)
             shorter-input (if (< a-len b-len)
                             a
                             b)]
         (concat (map longer-list longer-input shorter-input)
                 (map #(pad-list % 3 0) (drop (count shorter-input) longer-input)))))
  )

(defn remove-if-already-processed [data]
  (first (reduce (fn [[result previous] [a b c]]
                   [(if (contains? previous a)
                      result
                      (conj result [a b c]))
                    (conj previous a)])
                 [[] #{}]
                 data))
  )

(defn already-processed [data]
  (if (= (first (first data)) (first (second data)))
    (subvec data 2)
    (rest data)
    )
  )

(defn calculate-points [item data point level original-count]
  (cond (<= level original-count)
        [
         (cond (= level 1)
               (conj (conj item (+
                                  (* (count (relationship-by-level (first item) data 1)) point)
                                  (* (count (relationship-by-level (first item) data 2))
                                     (/ point 2))
                                  ))
                     (calculate-points (first (already-processed data)) (already-processed data) (/ point 2) (+ level 1) (count (already-processed data)))
                     )
               :else
               (cond (> (count (relationship-by-level (second item) data 1)) 0)
                     (conj (conj item (+
                                        (* (count (relationship-by-level (first item) data 1)) point)
                                        (* (count (relationship-by-level (first item) data 2))
                                           (/ point 2))
                                        ))
                           (calculate-points (first (already-processed data)) (already-processed data) (/ point 2) (+ level 1) (count (already-processed data)))
                           )
                     :else
                     (conj (conj item (+ 0 0))
                           (calculate-points (first (already-processed data)) (already-processed data) (/ point 2) (+ level 1) (count (already-processed data)))
                           )
                     )
               )
         ]
        )
  )

(defn calculate-ranking-points [data]
  (partition 3
             (remove nil?
                     (flatten
                       (calculate-points (first data) data 1.0 1 (count data))
                       )
                     )
             )
  )

(defn convert-vector-to-json-string [data result]
  (if (= 1 (count data))
    (str result "{\"inviter\": " (first (first data)) ", \"points\": " (last (first data)) "}\n" )
    (recur (rest data) (str result "{\"inviter\": " (first (first data)) ", \"points\": " (last (first data))  "},\n" ))
    )
  )

(defn extract-ranking [file-path]
  (let [original-data (extract-data-from-file
                        file-path)
        removed-invalid-data (remove-invalid-invitations original-data)]

    (str "{ \"data\": ["
         (convert-vector-to-json-string
           (sort-by first
                    (remove-if-already-processed
                      (merge-list original-data
                                  (calculate-ranking-points removed-invalid-data)
                                  )
                      )
                    ) ""
           ) "]}")
    )
  )
