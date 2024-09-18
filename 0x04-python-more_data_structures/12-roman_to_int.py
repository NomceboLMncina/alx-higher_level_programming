#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_i = 0
    for x in range(len(roman_string)):
        if x > 0 and rd[roman_string[x]] > rd[roman_string[x - 1]]:
            r_i += rd[roman_string[x]] - 2 * 1
                        rd[roman_string[x - 1]]
        else:
            r_i += rd[roman_string[x]]
    return r_i
