#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If too long, cut the tuple to the first 2 elements
    # if too short, extend the tuple to match length 2
    x = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    y = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    z = [i + j for i, j in zip(x, y)]
    return tuple(z[0:2])
