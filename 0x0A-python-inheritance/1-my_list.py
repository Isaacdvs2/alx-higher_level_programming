#!/usr/bin/python3
"""
A module contianing the MyList class that inherits from the list class
"""

class MyList(list):
    """is a subclass of list"""
    def __init__(self):
        """special method that initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted listin ascending order"""
        print(sorted(self))
