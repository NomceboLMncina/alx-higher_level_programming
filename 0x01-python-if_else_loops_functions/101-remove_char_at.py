#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    stringx = ""
    for j in str:
        if x != n:
            stringx += j
        x += 1
    return stringx
