#!/usr/bin/python2.7

def print_median(merged_list):
    if len(merged_list) % 2 == 0:
        med = len(merged_list)/2
        median = float((merged_list[med-1] + merged_list[med]))/2
    else:
        med = int((len(merged_list)//2))
        median = merged_list[med]
    print "median:", median

def merge_list(first_list, second_list, dedup=False):
    main_list, sub_list = first_list, second_list
    merged_list = []

    max_len = len(main_list)
    if main_list[-1] < sub_list[-1]:
        main_list, sub_list = second_list, first_list
        max_len = len(main_list)

    count = 0
    has_dup = False
    j = 0
    for i in range(max_len):
       while j < len(sub_list):
           print count, ":", merged_list
           count += 1
           if main_list[i] >= sub_list[j]:
               if dedup:
                   if main_list[i] == sub_list[j]:
                       has_dup = True
               if not has_dup:    
                   merged_list.append(sub_list[j])
               j += 1
           else:
               break

       merged_list.append(main_list[i])
       has_dup = False
    
       #print merged_list
    return merged_list



if __name__ == '__main__':
    list_1 = [3, 7, 9, 10, 23, 25, 26]
    list_2 = [1, 4, 5, 7, 12, 17, 23, 31]
    list_A = list_1
    list_B = list_2

    print("Merge list A and list B.")
    print("List A: lenght=%s, list=%s" % (len(list_A), list_A))
    print("List B: lenght=%s, list=%s" % (len(list_B), list_B))
    
    print "="*72

    print "- normal merge -"
    merged_list = merge_list(list_A, list_B)
    print "merged list:", merged_list
    print "length: %s" % len(merged_list)
    print_median(merged_list)

    print "-"*72

    print "- deduplicated merge-"
    merged_list = merge_list(list_A, list_B, dedup=True)
    print "merged list:", merged_list
    print "length: %s" % len(merged_list)
    print_median(merged_list)
