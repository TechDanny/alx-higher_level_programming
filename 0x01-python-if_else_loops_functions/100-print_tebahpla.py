#!/usr/bin/python3
for all_letters in range(122, 96, -1):
    if all_letters % 2 == 1:
        all_letters = all_letters - 32
    print("{:c}".format(all_letters), end="")
