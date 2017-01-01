def sort(list_of_items):
    for i in range(1, len(list_of_items)):
        current_value = list_of_items[i]
        position = i

        while position > 0 and list_of_items[position - 1] > current_value:
            list_of_items[position] = list_of_items[position - 1]
            position -= 1

        list_of_items[position] = current_value
