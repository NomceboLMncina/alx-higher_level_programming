#!/usr/bin/python3
def to_uper(i):
    if ord(i) >= 97 and ord(i) <= 122:
        return (ord(i) - 32)
    else:
        return ord(i)


def uppercase(str):
    j = ""
    for i in str:
        j += "%c" % to_uper(i)
    print("{:s}".format(j))
