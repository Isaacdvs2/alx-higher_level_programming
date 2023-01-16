#!/usr/bin/python3

""" This is a base class module """

class Base:
    """The base class for all other modules in the project.
        Its goal is to manage the id attribute """
    __nb_objects = 0
    def __init__(self, id = None):
        """ The constructor method for the base class. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
