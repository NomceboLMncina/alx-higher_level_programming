#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    r_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_n = 0
    for x in range(len(roman_string)):
        if x > 0 and r_d[roman_string[x]] > r_d[roman_string[x - 1]]:
            r_n += r_d[roman_string[x]] - 2 * r_d[roman_string[x - 1]]
        else:
            r_n += r_d[roman_string[x]]
    return r_n
