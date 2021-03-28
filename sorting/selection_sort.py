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

def selection_sort(list_data, descending=False):
   list_length = len(list_data)
   for i in range(0, list_length):
       least_index = i

       # find the smallest value and move to front
       for k in range(i+1, list_length):
           if descending:
               if list_data[least_index] < list_data[k]:
                   least_index = k
           else:
               if list_data[least_index] > list_data[k]:
                   least_index = k
           debug(list_data)
       debug(list_data)
       swap(list_data, least_index, i)


# ------------------------------------------------------------------------------

input_data = [16, 2, 13, 5, 11, 8, 9, 14, 17, 4, 1, 12, 18, 7, 15, 10, 3, 6]

print("[ Ascending sort ]\n"+"-"*80)
list_data = input_data[:]
print("- input   : %s" % list_data)
selection_sort(list_data)
print("- output  : %s" % list_data)

print()

print("[ Descending sort ]\n"+"-"*80)
list_data = input_data[:]
print("- input   : %s" % list_data)
selection_sort(list_data, descending=True)
print("- output  : %s" % list_data)
