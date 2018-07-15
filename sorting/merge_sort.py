#!/usr/bin/python3

enable_debug = True
count_debug = 0

def debug(msg):
    global enable_debug
    global count_debug
    if enable_debug:
        print("%s, count: %s" % (msg, count_debug))
        count_debug += 1

def merge_lists(left_list, right_list, descending=False):
    i = 0
    j = 0
    merged_list = []
    while i < len(left_list) and j < len(right_list):
        if descending:
            if left_list[i] >= right_list[j]:
                merged_list.append(left_list[i])
                i += 1
            else:
                merged_list.append(right_list[j])
                j += 1
        else:
            if left_list[i] <= right_list[j]:
                merged_list.append(left_list[i])
                i += 1
            else:
                merged_list.append(right_list[j])
                j += 1
    
    merged_list += left_list[i:]
    merged_list += right_list[j:]
    return merged_list 

def merge_sort(list_data, descending=False):
    list_length = len(list_data)
    if list_length <= 1:
        debug(list_data)
        return list_data
    if list_length == 2:
        if descending:
            if list_data[0] < list_data[1]:
                list_data[0], list_data[1] = list_data[1], list_data[0]
        elif list_data[0] > list_data[1]:
            list_data[0], list_data[1] = list_data[1], list_data[0]
        debug(list_data)
        return list_data

    middle_index = list_length // 2
    left_list = merge_sort(list_data[:middle_index], descending=descending)
    right_list = merge_sort(list_data[middle_index:], descending=descending)
    debug(list_data)
    return merge_lists(left_list, right_list, descending=descending)


input_data = [16, 2, 13, 5, 11, 8, 9, 14, 17, 4, 1, 12, 18, 7, 15, 10, 3, 6]

print("Ascending sort:")
print("- input   : %s" % input_data)
output = merge_sort(input_data)
print("- output  : %s" % output)

print("Descending sort:")
print("- input   : %s" % input_data)
output = merge_sort(input_data, descending=True)
print("- output  : %s" % output)
