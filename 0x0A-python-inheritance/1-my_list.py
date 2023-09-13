#!/usr/bin/python3
# By - Musonda Christopher
# A Python class MyList that inherits from list.
"""Defines an inherited list class MyList."""
class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
