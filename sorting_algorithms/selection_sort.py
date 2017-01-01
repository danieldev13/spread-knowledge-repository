def sort(list_of_items):
    for fill_slot in range(len(list_of_items) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if list_of_items[location]>list_of_items[position_of_max]:
                position_of_max = location
        temp = list_of_items[fill_slot]
        list_of_items[fill_slot] = list_of_items[position_of_max]
        list_of_items[position_of_max] = temp

