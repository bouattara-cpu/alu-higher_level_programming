#!/usr/bin/python3
"""Safe integer print with error message module"""
import sys


def safe_print_integer_err(value):
    """Print value as integer, return True/False, print errors to stderr"""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
