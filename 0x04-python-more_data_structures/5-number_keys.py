#!/usr/bin/python3


def number_keys(a_dictionary):
    """returns the number of keys in a dictionary."""
    keys = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        keys += 1

    return (keys)
