#!/usr/bin/python3
import sys


def get_status():
    """
    show status
    """
    numb = 0
    size = 0
    fsize = 0
    status_code = {"200": 0, "301": 0, "400": 0, "401": 0, "402": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}
    for n in sys.stdin:
        file_line = n.split()
        try:
            size = int(file_line[-1])
            cd = file_line[-2]
            status_codes[cd] = status_codes[cd] + 1
        except ValueError:
            continue
        if numb == 9:
            print("File size: {}".format(size))
            for k, v in sorted(status_code.items()):
                if (v != 0):
                    print("{}: {}".format(k, v))
            numb = 0
        numb = numb + 1
        if numb < 9:
            print("File size: {}".format(size))
            for k, v in sorted(status_code.items()):
                if (v != 0):
                    print("{}: {}".format(k, v))


if __name__ == "__main__":
    get_status()
