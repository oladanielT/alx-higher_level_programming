#!/usr/bin/python3
"""Defines function that appends a string at the end of a text"""


def append_write(filename="", text=""):
    """Appending a string to a file.
    Parameters:
        filename (str).
        text (str).
    Return:
        number of characters and the appended lists.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
