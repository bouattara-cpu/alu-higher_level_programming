#!/usr/bin/python3
"""Module that defines a MyList class."""


class Mylist(list):
    """Represent a list.

    This class inherits from the built-in list class and adds
    a method to print the list in sorted order.
    """

    def print_sorted(self):
        """Print the list, sorted in ascending order."""
        print (sorted(self))
