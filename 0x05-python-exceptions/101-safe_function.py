#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Execute a function safely.

    Args:
        fct: function to execute.
        args: Args for fct.

    Returns:
        If an error occurs return None.
        Otherwise return the result of the call to fct.
    """
    try:
        res = fct(*args)
        return (res)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
