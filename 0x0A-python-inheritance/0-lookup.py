#!/usr/bin/python3

"""A class returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """returns the list of available attributes"""
    return dir(obj)
