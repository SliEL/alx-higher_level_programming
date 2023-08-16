#!/usr/bin/python3


def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)"""
    unique_list = set(my_list)
    num = 0

    for i in unique_list:
        num += i

    return (num)
