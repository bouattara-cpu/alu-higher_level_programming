#!/usr/bin/python3
"""Safe function module"""
import sys


def safe_function(fct, *args):
    """Execute fct safely, return its result or None on exception"""
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
