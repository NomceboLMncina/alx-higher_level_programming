#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import *
    c = len(argv)

    if c != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    n1 = int(argv[1])
    n2 = int(argv[3])
    operation = argv[2]

    def not_found():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def add_():
        total = add(n1, n2)
        print("{:d} + {:d} = {:d}".format(n1, n2, total))
        return total

    def sub_():
        total = sub(n1, n2)
        print("{:d} - {:d} = {:d}".format(n1, n2, total))
        return total

    def mul_():
        total = mul(n1, n2)
        print("{:d} * {:d} = {:d}".format(n1, n2, total))
        return total

    def div_():
        total = div(n1, n2)
        print("{:d} / {:d} = {:d}".format(n1, n2, total))
        return total

    options = {
        "+": add_,
        "-": sub_,
        "*": mul_,
        "/": div_
    }
    options.get(operation, not_found)()
