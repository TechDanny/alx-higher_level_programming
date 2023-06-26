#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        r = fct(*args)
    except Exception as n:
        sys.stderr.write("Exception: {}\n".format(n))
        r = None
    return r
