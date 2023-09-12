#!/usr/bin/python3
"""Module that defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file.

    Args:
        filename (str): Name of the file.
        search_string (str): The target string to look for.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)