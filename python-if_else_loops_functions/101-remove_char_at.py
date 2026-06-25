#!/usr/bin/python3
"""Module that defines remove_char_at."""


def remove_char_at(str, n):
    """Return a new string with the character at index n removed.

    If n is negative or out of range, the string is returned unchanged.
    """
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n + 1:]
