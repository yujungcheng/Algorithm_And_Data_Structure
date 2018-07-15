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

def sift_down(list_data, parent_index, list_length, descending=True):
    while True:
        left_child_index = 2 * parent_index + 1
        right_child_index = left_child_index + 1
        parent = parent_index
 
        if descending:
            if left_child_index < list_length:
                if list_data[left_child_index] > list_data[parent]:
                    parent = left_child_index
            if right_child_index < list_length:
                if list_data[right_child_index] > list_data[parent]:
                    parent = right_child_index
        else:
            if left_child_index < list_length:
                if list_data[left_child_index] < list_data[parent]:
                    parent = left_child_index
            if right_child_index < list_length:
                if list_data[right_child_index] < list_data[parent]:
                    parent = right_child_index

        if parent == parent_index:
            break
        swap(list_data, parent_index, parent)
        parent_index = parent

def heapify(list_data, descending=True):
    list_length = len(list_data)
    least_parent = list_length // 2 - 1  # get least index of parent node
    while least_parent >= 0:
        if descending:
            sift_down(list_data, least_parent, list_length)
        else:
            sift_down(list_data, least_parent, list_length, descending=False)
        least_parent -= 1
        debug(list_data)

def heap_sort(list_data, descending=False):
    # transform to heap list 
    if descending:
        heapify(list_data, descending=False)
    else:
        heapify(list_data)

    print("- heapify : %s" %list_data)

    last_index = len(list_data) - 1
    for i in range(last_index, 0, -1):
        if descending:
            if list_data[0] < list_data[i]:
                swap(list_data, 0, i)
                sift_down(list_data, 0, i-1, descending=False)
        else:
            if list_data[0] > list_data[i]:
                swap(list_data, 0, i)
                sift_down(list_data, 0, i-1)
        debug(list_data)


input_data = [16, 2, 13, 5, 11, 8, 9, 14, 17, 4, 1, 12, 18, 7, 15, 10, 3, 6]

print("Ascending sort") 
list_data = input_data[:]
print("- input   : %s" % list_data)
heap_sort(list_data)
print("- output  : %s" % list_data)

print("Descending sort")
list_data = input_data[:]
print("- input   : %s" % list_data)
heap_sort(list_data, descending=True)
print("- output  : %s" % list_data)

