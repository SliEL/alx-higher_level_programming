#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x int elements of a list.

    Args:
        my_list (list): List to print elements from.
        x (int): The num of elements of the list to print.

    Returns:
        The number of elements printed.
    """
    total = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            total += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (total)
