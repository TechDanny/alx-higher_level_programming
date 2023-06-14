#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    is_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 100
    }
    previous_num = 0
    total_sum = 0
    for n in range(len(roman_string) - 1, -1, -1):
        current_num = is_roman.get(roman_string[n], 0)
        if current_num >= previous_num:
            total_sum += current_num

        else:
            total_sum -= current_num

        previous_num = current_num
    return total_sum
