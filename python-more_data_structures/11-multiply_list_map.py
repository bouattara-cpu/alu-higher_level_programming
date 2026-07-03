#!/usr/bin/python3
"""Module that defines a function to multiply list values using map."""


def multiply_list_map(my_list=[], number=0):
    """Return a new list with values multiplied by number, using map."""
    return list(map(lambda x: x * number, my_list))
