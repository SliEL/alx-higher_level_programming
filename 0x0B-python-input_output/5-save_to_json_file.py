#!/usr/bin/python3
"""Defines an obj to a file using json repr"""

import json

def save_to_json_file(my_obj, filename):
    """writes an obj to text file in json repr.
    
    Args:
        my_obj: object to write to the file.
        filename: the file to write to.
    
    """
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(my_obj, file)