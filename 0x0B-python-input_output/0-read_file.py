#!/usr/bin/python3

""" A module that reads a txt file and displays
its contents to std out """

def read_file(file_name=""):
    """ A method that takes the filename as input and displays it
    to std out """
    with open(file_name, encoding = "utf-8") as f:
        print(f.readlines(), end = "")
