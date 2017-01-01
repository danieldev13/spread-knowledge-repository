def sort(list_of_items):
    for passing_number in range(len(list_of_items) - 1, 0, -1):
        for i in range(passing_number):
            if list_of_items[i] > list_of_items[i+1]:
                temp = list_of_items[i]
                list_of_items[i] = list_of_items[i+1]
                list_of_items[i+1] = temp


def sort2(list_of_items):
    exchanges = True
    passing_number = len(list_of_items) - 1

    while passing_number > 0 and exchanges:
        exchanges = False
        for i in range(passing_number):
            if list_of_items[i] > list_of_items[i+1]:
                exchanges = True
                temp = list_of_items[i]
                list_of_items[i] = list_of_items[i+1]
                list_of_items[i+1] = temp

        passing_number -= 1
