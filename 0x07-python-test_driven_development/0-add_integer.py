#!/usr/bin/python3
"""Function that Defines addition of two ints."""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.

    Float args accepted and typecasted to ints before addition is performed.

    Args:
        a,b (int or float): numbers to add.

    Raises:
        TypeError: If a or b is a non-integer and non-float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
