#!/usr/bin/python3
if __name__ == "__main__":
    from magic_calculation_102 import sub, add
    if a < b:
        c = add(a, b)
        for n in range(5, 8):
            c = add(c, 1)
        return c
    else:
        return sub(a, b)
