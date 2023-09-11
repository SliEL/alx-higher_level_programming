#!/usr/bin/python3
"""defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the builtin list class."""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))