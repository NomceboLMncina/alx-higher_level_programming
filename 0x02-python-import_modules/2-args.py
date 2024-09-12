#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    SUM = len(sys.argv)
    if SUM <= 1:
        print("0 arguments.")
    else:
        if SUM == 2:
            print("{:d} argument:".format(SUM - 1))
        else:
            print("{:d} arguments:".format(SUM - 1))
        for x in range(1, SUM):
            print("{:d}: {}".format(x, sys.argv[x]))
