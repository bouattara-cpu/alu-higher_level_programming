#!/usr/bin/python3
"""Module that deletes keys with a specific value in a dictionary."""


def complex_delete(a_dictionary, value):
    """Return a new dictionary with keys matching value removed."""
    return {k: v for k, v in a_dictionary.items() if v != value}
