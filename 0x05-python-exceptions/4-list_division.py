#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divide 2 lists element by element.

    Args:
        my_list_1 (list): first list.
        my_list_2 (list): second list.
        list_length (int): number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for index in range(0, list_length):
        try:
            res = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return (new_list)
