#!/usr/bin/python3
"""Defines a function that appends text to end of a file."""

def append_write(filename='', text=''):
    """Appends text to end of utf8 file.
    
    Args:
        filename (str): file name to append text to.
        text (str): text to append to the end of the file.
    Return:
        The number of chars added to the file.
    """

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)