#!/usr/bin/python3

"""
A rectangle module that inherits from the Base geometry module.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A rectangle class that inherits from the base Geometry class"""

    def __init__(self, width, height):
        """ initialise the rect class """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def Area(self):
        """ The method to return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """A str method that returns the rectangle dewcription """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

