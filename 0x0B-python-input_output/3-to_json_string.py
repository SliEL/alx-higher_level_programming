#!/usr/bin/python3
"""Returns the Json representation of an object."""

import json

def to_json_string(my_obj):
    """Returns the json repr of the obj.

    Args:
        my_obj: the target object.
    Returns:
        the json repr of the obj.
    """
    return json.dumps(my_obj)