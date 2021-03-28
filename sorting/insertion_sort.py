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

def insertion_sort(list_data, descending=False):
    list_length = len(list_data)

    for i in range(1, list_length):
        temp_value = list_data[i]
        value_index = i

        while value_index > 0:
            if descending:
                if list_data[value_index-1] < list_data[value_index]:
                    swap(list_data, value_index, value_index-1)
                else:
                    break
            else:
                if list_data[value_index-1] > list_data[value_index]:
                    swap(list_data, value_index, value_index-1)
                else:
                    break
            value_index -= 1
            debug(list_data)

def insertion_sort_1(list_data, descending=False):
    list_length = len(list_data)

    for i in range( 1, list_length ):
        temp_value = list_data[i]
        value_index = i
        if descending:
            while value_index > 0 and temp_value > list_data[value_index-1]:
                list_data[value_index] = list_data[value_index-1]
                value_index -= 1
        else:
            while value_index > 0 and temp_value < list_data[value_index-1]:
                list_data[value_index] = list_data[value_index-1]
                value_index -= 1
        list_data[value_index] = temp_value


# ------------------------------------------------------------------------------

input_data = [16, 2, 13, 5, 11, 8, 9, 14, 17, 4, 1, 12, 18, 7, 15, 10, 3, 6]

print("[ Ascending sort ]\n"+"-"*80)
list_data = input_data[:]
print("- input   : %s" % list_data)
insertion_sort(list_data)
print("- output  : %s" % list_data)

print()

print("[ Descending sort ]\n"+"-"*80)
list_data = input_data[:]
print("- input   : %s" % list_data)
insertion_sort(list_data, descending=True)
print("- output  : %s" % list_data)
