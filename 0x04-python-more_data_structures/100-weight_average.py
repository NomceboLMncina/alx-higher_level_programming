#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return sum([i*j for (i, j) in my_list]) / sum([j for (i, j) in my_list])
