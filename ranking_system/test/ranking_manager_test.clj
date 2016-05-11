 (ns ranking-manager-test
   (:use [clojure.test]
         [clojure.test.junit]
         [reward-system-business.ranking-manager])
   )

(def test-data-mock
  [[1 2] [1 3] [3 4] [2 4] [4 5] [4 6]])

(def test-data-invalid-removed-mock
  [[1 2] [1 3] [3 4] [4 5] [4 6]])

(def test-data-ranking-mock
  [[1 2 2.5] [3 4 1] [4 5 0]])

(deftest test-remove-invalid-invitations
         (assert
           (= [[1 2] [1 3] [3 4] [4 5] [4 6]] (remove-invalid-invitations test-data-mock))
           )
         )

(deftest test-relationship-by-level-1
         (assert
           (= [[1 2] [1 3]] (relationship-by-level 1 test-data-mock 1))
           )
         )

(deftest test-relationship-by-level-2
         (assert
           (= [[2 4] [3 4]] (relationship-by-level 1 test-data-mock 2))
           )
         )

(deftest test-merge-list
         (assert
           (= [[1 2 2.5] [3 4 1] [4 5 0] [2 4 0] [4 5 0] [4 6 0]] (merge-list test-data-mock test-data-ranking-mock))
           )
         )

(deftest test-calculate-ranking-points
         (assert
           (= [(1 2 2.5) (3 4 1.0)] (vec (calculate-ranking-points test-data-invalid-removed-mock)))
           )
         )

(run-all-tests)
