#!/usr/bin/python3

"""
File: 101-add_attribute.py
Desc: This module  contains a function defination
Author: Muzzo
Date Created: Sept 2023
"""


def add_attribute(obj, att, value):
    """
    a funct adds a new attribute to object if it’s possible.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add niew attribute")
