#!/usr/bin/python3
"""Defines a function that return an object by aJSON string"""
import json


def from_json_string(my_str):
    """
    Represent a function that return object rep.
    Paremeter:
     my_str (str)
    """
    return json.loads(my_str)
