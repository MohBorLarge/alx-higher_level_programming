#!/usr/bin/python3
"""returns json representation of an object(string)"""
import json


def to_json_string(my_obj):
    """returns the json representation of an object"""
    da = json.dumps(my_obj)
    return da
