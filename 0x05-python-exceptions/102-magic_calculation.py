#!/usr/bin/python3
def magic_calculation(a, b):
    reslt = 0
    for n in range(1, 3):
        try:
            if (n > a):
                raise Exception('Too far')
            else:
                reslt = reslt + (a**b) / n
        except Exception:
            reslt = a + b
            break
    return(reslt)
