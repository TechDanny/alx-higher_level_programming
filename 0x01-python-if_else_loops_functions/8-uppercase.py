#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - (ord('a') - ord('A')))
        print(f"{(c):s}" ,end="")
    print("")
