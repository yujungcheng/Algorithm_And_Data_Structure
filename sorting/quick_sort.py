#!/usr/bin/python3

enable_debug = True
count_debug = 0

def debug(msg):
    global enable_debug
    global count_debug
    if enable_debug:
        print("%s, count: %s" % (msg, count_debug))
        count_debug += 1

def swap(list_data, x, y):
    list_data[x], list_data[y] = list_data[y], list_data[x]

def partition(list_data, first_index, last_index, descending):
    pivot_value = list_data[first_index]
    start_index = first_index + 1
    pivot_index = start_index

    for j in range(first_index+1, last_index+1):
        if descending:
            if list_data[j] > pivot_value:
                swap(list_data, start_index, j)
                start_index += 1
        else:
            if list_data[j] < pivot_value:
                swap(list_data, start_index, j)
                start_index += 1
        debug(list_data)

    pivot_index = start_index - 1
    swap(list_data, first_index, pivot_index)
    debug(list_data)
    return pivot_index

def _quick_sort(list_data, first_index, last_index, descending):
    if first_index < last_index:
        split_index = partition(list_data,
                                first_index,
                                last_index,
                                descending)
        _quick_sort(list_data, first_index, split_index-1, descending)
        _quick_sort(list_data, split_index+1, last_index, descending)

def quick_sort(list_data, descending=False):
    return _quick_sort(list_data, 0, len(list_data)-1, descending)


# ------------------------------------------------------------------------------

input_data = [16, 2, 13, 5, 11, 8, 9, 14, 17, 4, 1, 12, 18, 7, 15, 10, 3, 6]

print("[ Ascending sort ]\n"+"-"*80)
list_data = input_data[:]
print("- input   : %s" % list_data)
quick_sort(list_data)
print("- output  : %s" % list_data)

print()

print("[ Descending sort ]\n"+"-"*80)
list_data = input_data[:]
print("- input   : %s" % list_data)
quick_sort(list_data, descending=True)
print("- output  : %s" % list_data)
