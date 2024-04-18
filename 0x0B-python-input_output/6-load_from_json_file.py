#!/usr/bin/python3
""" function that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a JSON file.
    Args:
        filename (str).
    """
    with open(filename) as file:
        return json.load(file)
