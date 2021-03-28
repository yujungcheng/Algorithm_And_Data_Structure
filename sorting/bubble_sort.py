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

def bubble_sort(list_data, descending=False):
    list_length = len(list_data)
    for i in range(list_length):
        for j in range(list_length-1, i, -1):
            right_index = j
            left_index = j - 1
            if descending:
                if list_data[left_index] < list_data[right_index]:
                    swap(list_data, left_index, right_index)
            else:
                if list_data[left_index] > list_data[right_index]:
                    swap(list_data, left_index, right_index)
            debug(list_data)

def bubble_sort_1(list_data, descending=False):
    list_length = len(list_data)
    for i in range(list_length):
        for j in range(list_length-1, 0, -1):
            right_index = j
            left_index = j - 1
            if list_data[left_index] > list_data[right_index]:
                swap(list_data, left_index, right_index)
            debug(list_data)


# ------------------------------------------------------------------------------

input_data = [16, 2, 13, 5, 11, 8, 9, 14, 17, 4, 1, 12, 18, 7, 15, 10, 3, 6]

print("[ Ascending sort ]\n"+"-"*80)
list_data = input_data[:]
print("- input   : %s" % list_data)
bubble_sort(list_data)
print("- output  : %s" % list_data)

print()

print("[ Descending sort ]\n"+"-"*80)
list_data = input_data[:]
print("- input   : %s" % list_data)
bubble_sort(list_data, descending=True)
print("- output  : %s" % list_data)
