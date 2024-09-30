#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):
    if my_list is None:
        my_list = []
    t = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            t += 1
        except IndexError:
            break
    print()
    return t
