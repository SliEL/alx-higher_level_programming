#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Prints an int with "{:d}".format().

    If a ValueError message occurs, a corresponding
    message is printed to standard error.

    Args:
        value (int): The int value to print.

    Returns:
        If a TypeError or ValueError occurs return False.
        Otherwise return True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
