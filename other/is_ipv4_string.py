#!/usr/bin/python3

import sys, re


def main(argv_list):
    if len(argv_list) == 1:
        print("Please enter at least a IPv4 address.")
        return 2
    argv_item = argv_list[1:]

    re_str1 = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    re_str2 = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    re_str3 = "\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    re_str4 = "\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"

    ipv4_pattern = re.compile(re_str1)

    for argv_value in argv_item:
        if ipv4_pattern.match(argv_value):
            print("%s is valid." % argv_value)
        else:
            print("%s is invalid." % argv_value) 
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
