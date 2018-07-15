#!/usr/bin/python2.7

import sys

# find two index of values that sum up with a target value.

def main():

    int_list = [4, 5, 7, 2, 3]
    target = 8
    print("integer list: %s" % int_list)
    print("target      : %s" % target)

    complement_map = dict()
    for i in range(len(int_list)): 
        complement = target - int_list[i]
        if complement_map.has_key(complement):
            print("found indexs: int_list[%s]=%s and int_list[%s]=%s" % (
                  i, int_list[i], complement_map[complement], complement))
            return 0
        complement_map[int_list[i]] = i
    return 1

if __name__ == '__main__':
    sys.exit(main())
