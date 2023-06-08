#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    if num == 0:
        print("{} arguments.".format(num))
    elif num == 1:
        print("{} arguments:".format(num))
    else:
        print("{} arguments:".format(num))
    for x in range(num):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
