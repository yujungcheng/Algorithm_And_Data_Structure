#!/usr/bin/python2.7

import sys


def add_one(input_array):
    #raw_array = input_array[:] # another way to copy list
    raw_array = list(input_array)
    carry = 1
    for i in range(len(input_array)-1, -1, -1):
        new_num = input_array[i] + carry
        if new_num >= 10:
            input_array[i] = 0
        else:
            carry = 0
            input_array[i] = new_num
    if carry == 1:
        print raw_array, "+ 1 ->" , [1] + input_array
    else:
        print raw_array, "+ 1 ->", input_array

if __name__ == '__main__':
    array_1 = [1, 2, 3]
    array_2 = [1, 2, 9]
    array_3 = [1, 9, 9]
    array_4 = [9, 9, 9]
    arrays = [array_1, array_2, array_3, array_4]
    for i in range(len(arrays)):
        add_one(arrays[i])
    
