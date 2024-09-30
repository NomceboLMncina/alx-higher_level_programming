#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            else:
                r += a ** b / x
        except Exception:
            r = b + a
            break
    return r
