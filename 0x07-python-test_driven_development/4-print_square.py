#!/usr/bin/python3
def print_square(size):
    """
    prints a square character with #
    """
    if not isinstance(size, int):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
