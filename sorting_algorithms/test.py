import selection_sort
import bubble_sort
import insertion_sort


def test_selection_sort():
    list_of_items = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(list_of_items)
    selection_sort.sort(list_of_items)
    print(list_of_items)


def test_bubble_sort():
    list_of_items = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(list_of_items)
    bubble_sort.sort(list_of_items)
    print(list_of_items)


def test_bubble_sort2():
    list_of_items = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(list_of_items)
    bubble_sort.sort2(list_of_items)
    print(list_of_items)


def test_insertion_sort():
    list_of_items = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(list_of_items)
    insertion_sort.sort(list_of_items)
    print(list_of_items)


print('testing selection sort...')
test_selection_sort()

print('testing bubble sort...')
test_bubble_sort()

print('testing bubble sort2...')
test_bubble_sort2()

print('testing insertion sort...')
test_insertion_sort()
