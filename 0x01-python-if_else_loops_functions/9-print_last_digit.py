#!/usr/bin/python3
def print_last_digit(x):
    if x < 0:
        x *= -1
    j = x % 10
    print('{:d}'.format(j), end='')
    return j
