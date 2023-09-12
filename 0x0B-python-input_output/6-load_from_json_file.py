#!/usr/bin/python3
"""Defines an Object from a json file."""

import json

def load_from_json_file(filename):
    """creates an object from json file."""
    with open(filename) as file:
        return json.load(file)