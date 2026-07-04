#!/usr/bin/python3
"""ByteCode -> Python #4 module"""


def magic_calculation(a, b):
    """Perform the calculation described by the given bytecode"""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
