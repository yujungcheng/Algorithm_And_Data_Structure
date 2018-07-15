#!/usr/bin/python2.7


def second_onwards_deduplicate(input_list):
    # {"data_string": count, ... }
    data_count = dict()
    
    index = 0
    while index < len(input_list):
        key = input_list[index]
        if data_count.has_key(key):
            if data_count[key] >= 2:
                del input_list[index]
                continue
            else:
                data_count[key] += 1
        else:
            data_count[key] = 1
        
        index += 1
    return input_list

if __name__ == '__main__':
    input_list = ['aa', 'bb', 'cc', 'aa', 'cc', 'bb', 'dd', 'aa', 'cc', 'ee', 'aa']
    print("input : %s"% input_list)
    output_list = second_onwards_deduplicate(input_list)
    print("output: %s"% output_list)
