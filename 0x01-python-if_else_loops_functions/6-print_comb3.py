#!/usr/bin/python3
for numbers in range(0, 9):
    for nums in range(numbers+1, 10):
        print("{}{}".format(numbers, nums), end=", ")
print("{}{}".format(numbers, nums))
