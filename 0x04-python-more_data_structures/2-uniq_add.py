#!/usr/bin/python3
def uniq_add(my_list=[]):
    list2 = list(set(my_list))
    total_sum = 0
    for i in list2:
        total_sum += i
    return total_sum
