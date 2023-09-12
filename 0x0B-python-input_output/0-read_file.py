#!/usr/bin/python3
"""Defines a function to read text file."""

def read_file(filename=''):
    """prints the content of a text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')