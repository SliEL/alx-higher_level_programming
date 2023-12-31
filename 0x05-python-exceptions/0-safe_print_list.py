#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): List to print elements from.
        x (int): The num of elements to print.

    Returns:
        The num of elements printed.
    """
    total = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            total += 1
        except IndexError:
            break
    print("")
    return (total)
