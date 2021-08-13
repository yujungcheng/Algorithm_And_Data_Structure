#!/usr/bin/env python
""" get arithemtic mean of field X in csv file """

import sys


# write csv data file
csv_data = """1,2,3,4,5
10,"a,b",10,20,30,40,50
6,7,8,9,10
"""

csv_file = "./data.csv"
with open(csv_file, "w") as f:
    f.write(csv_data)


def main(argv):
    count = mean = sum = 0
    target_field = int(argv[1])  # get which filed to sum up values

    with open(csv_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            line_data = line.strip().split(",")
            new_field = target_field
            field_count = 0
            for data in line_data:  # handle delimiterissue
                if not data.isdigit():
                    new_field += 1
                field_count += 1
                if field_count+1 == target_field:
                    break
            if new_field != target_field:
                new_field -= 1
            count += 1
            sum += int(line_data[new_field])
            print("%s - add %s" % (count, line_data[new_field]))

    mean = sum/count
    print("Sum: %s, Count: %s, Mean: %s" % (sum, count, mean))


if __name__ == "__main__":
    main(sys.argv)
