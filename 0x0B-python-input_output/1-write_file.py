#!/usr/bin/python3
"""Defines a function that write a string to a file
    And returns the number of chars written.
"""

def write_file(filename='', text=''):
    """writes a text to a utf8 file.
     
    Args:
        filename (str): the file name to write to.
        text (str): text to write to the file.
    Return: 
        num of chars written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
