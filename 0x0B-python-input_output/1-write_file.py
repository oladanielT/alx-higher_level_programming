#!/usr/bin/python3
"""Defines a function to write"""


def write_file(filename="", text=""):
    """Write a text.
    Parameters:
        filename (str): file to write to.
        text (str): text we want to write to a file.
    Return:
        Number of characters.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
