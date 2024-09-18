#!/usr/bin/python3
def print_sorted_dictionary(dictionary):
    for x in sorted(dictionary):
        print("{:s}: {}".format(x, dictionary[x]))
