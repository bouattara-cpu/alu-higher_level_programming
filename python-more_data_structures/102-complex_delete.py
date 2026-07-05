#!/usr/bin/python3
"""Module that deletes keys with a specific value in a dictionary."""


def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary, in place."""
    keys_to_delete = [k for k, v in a_dictionary.items() if v == value]
    for k in keys_to_delete:
        del a_dictionary[k]
    return a_dictionary
