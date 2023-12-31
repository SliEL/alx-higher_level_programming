#!/usr/bin/python3
"""Defines a function that returns an object from json string."""

import json

def from_json_string(my_str):
    """Returns an object from json string."""
    return json.loads(my_str)