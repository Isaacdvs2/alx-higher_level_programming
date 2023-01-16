#!/usr/bin/python3

""" The rectangle module for handling rectangle related stuff"""
#import the base class from the base module
from models.base import Base

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

    def area(self):
        """ the area function computes the area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """" The display method that prints the rectangle instance with the 
        character #.i.e., using the height and width, print the shape of the rectangle """
        shape = self.y * "\n"
        for i in range(self.height):
            shape += (" " * self.x)
            shape += ("#" * self.width) + "\n"
        print(shape, end='')

    def __str__(self):
        """ This method overrides the built-in method to return the string
        representation of the rectangle class. The desired output is [Rectangle] (<id>) <x>/<y> - <width>/<height> """

        rect_str = "[Rectangle] "
        rect_id = "({}) ".format(self.id)
        rect_pos = "{}/{} - ".format(self.x, self.y)
        rect_dims = "{}/{}".format(self.width, self.height)

        return rect_str + rect_id + rect_pos + rect_dims

    def update(self, *args, **kwargs):
        """ the method to update the rectangle's properties. accepts variable number
        of args"""
        # check if args were passed
        if args is not None and len(args) is not 0:
            list_attr = ['id', 'width', 'height', 'x', 'y']
            # if args were passed, set their order using the setattr method
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
