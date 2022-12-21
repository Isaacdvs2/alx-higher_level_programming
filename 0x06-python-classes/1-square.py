#!/usr/bin/python3

"""SA program to define a square of size "size" """


class Square:
    """A class that defines a square
    Attributes:
        __size (int): the size of the square's sides
    """
    def __init__(self, size):
        """Initializes the square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size

