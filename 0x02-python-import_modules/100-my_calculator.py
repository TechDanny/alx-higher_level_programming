#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, mul, div, add
    import sys
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators = {"-": sub, "*": mul, "/": div, "+": add}
    if sys.argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, operators[sys.argv[2]](a, b)))
