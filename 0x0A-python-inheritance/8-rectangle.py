#!/usr/bin/python3

"""
A rectangle module that inherits from the Base geometry module.
"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry

class Rectangle(BaseGeometry):
    """A rectangle class that inherits from the base Geometry class"""

    def __init__(self, width, height):
        """ initialise the rect class """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
