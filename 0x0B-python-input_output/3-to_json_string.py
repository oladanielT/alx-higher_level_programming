#!/usr/bin/python3
"""Defines a function that print JSON rep of a str"""
import json


def to_json_string(my_obj):
    """Representing JSON for strings.

    Parameter:
        my_obg : object to represent.
    """
    return json.dumps(my_obj)
