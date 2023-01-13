#!/usr/bin/python3

""" The script to write text to a txt file """

def write_file(filename="", text=""):
    """ A function to write text to a file and return
    the number of chars written to it """
    with open(filename, mode="w+", encoding = "UTF8") as my_file:
        return(my_file.write(text))
