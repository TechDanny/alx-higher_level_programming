#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult_nums = []
    for i in my_list:
        if i % 2 == 0:
            mult_nums.append(True)
        else:
            mult_nums.append(False)
    return mult_nums
