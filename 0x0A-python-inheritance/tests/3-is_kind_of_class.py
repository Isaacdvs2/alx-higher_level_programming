#!/usr/bin/python3
"""
A module to identify which class an instance belongs to
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance of or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
