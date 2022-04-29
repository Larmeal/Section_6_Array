# merge number between of [0, 3, 4, 31] and [4, 6, 30]
# sort in ascending order

array_1 = [0, 3, 4, 31]
array_2 = [-1, 4, 6, 30, 2]

def search_number(set_3):
    smallest = set_3[0]
    smallest_index = 0
    for i in range(1, len(set_3)):
        if set_3[i] < smallest:
            smallest = set_3[i]
            smallest_index = i
    return smallest_index

def selection_sort(set_1, set_2):
    merge_list = set_1 + set_2
    new_arr = []
    for i in range(len(merge_list)):
        smallest = search_number(merge_list)
        new_arr.append(merge_list.pop(smallest))
    return print(new_arr)


selection_sort(array_1, array_2)

# -------------------------------------------------------------

def selection_sort_2(set_1, set_2):
    merge_list = set_1 + set_2
    new_list = []
    test = 0
    for k in range(len(merge_list)):
        if test < merge_list[k]:
            arr_max = merge_list[k]
            test = merge_list[k]

    for i in range(len(merge_list)):
        arr = arr_max
        for j in merge_list:
            if j < arr:
                arr = j
        new_list.append(arr)
        merge_list.pop(merge_list.index(arr))

    print(new_list)
    
selection_sort_2(array_1, array_2)
# -------------------------------------------------------------

def selection_sort_3(set_1, set_2):
    merge_list = set_1 + set_2
    merge_list.sort(reverse=False)
    print(merge_list)

selection_sort_3(array_1, array_2)