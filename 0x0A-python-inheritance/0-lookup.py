#!/usr/bin/python3
# By - Musonda Christopher
# A Python function that returns the list of available attributes and methods of an object.
"""Defines an object attribute lookup function."""
def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
