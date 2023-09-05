#!/usr/bin/python3
"""Module that finds the max integer in a list"""


def max_integer(list=[]):
    """A function to find and return the max integer in a list of integers
        If list is empty,  return None
    """
    if len(list) == 0:
        return None
    result = list[0]
    index = 1
    while index < len(list):
        if list[index] > result:
            result = list[index]
        index += 1
    return result
