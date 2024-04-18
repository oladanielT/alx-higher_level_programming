#!/usr/bin/python3
"""Defines a function that writes an Object to a text file, using a JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """Writing an object to a text file.
    parameters:
        my_obj : objects to write.
        filename : text file.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
