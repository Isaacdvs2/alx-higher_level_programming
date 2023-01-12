#!/usr/bin/python3

""" A square module that inherits from the rectangle class """

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ A square class that handles square creation"""

    def __init__(self, size):
        """The constructor for the square class"""
        self.__size = size
        super()__init__(size, size)
        self.integer_validator("size", size)

    def area(self):
        """the area of the square"""
        return (self.__size * self.__size)
