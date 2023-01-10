#!/usr/bin/python3
"""
This module helps to identify if an object is of a specified class
"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of the specified class,  otherwise False"""
    return (type(obj) == a_class)

