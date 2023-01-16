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
        # validation method for the width value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for the height """
        return (self.__height)

    @height.setter
    def height(self, value):
         """ setter method for the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ the getter method for the x value"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ the setter method for the x value """
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """ the getter method for the y value """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ the setter method for the y value """
        if y < 0:
            raise ValueError("y must be >= 0")
