#!/usr/bin/python3

""" The rectangle module for handling rectangle related stuff"""

class Rectangle(Base):
    """ the clsaa rectangle is a subclass of the base class with
    height and width """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ the constructor method for the rectangle class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter method for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter method for the width """
        self.__width = value

    @property
    def height(self):
        """ getter method for the height """
        return (self.__height)

    @height.setter
    def height(self, value):
         """ setter method for the height """
        self.__height = value
