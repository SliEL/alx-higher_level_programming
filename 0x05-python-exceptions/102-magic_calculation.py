#!/usr/bin/python3


def magic_calculation(a, b):
    res = 0
    for index in range(1, 3):
        try:
            if index > a:
                raise Exception('Too far')
            else:
                res += a ** b / index
        except:
            res = b + a
            break
    return (res)
