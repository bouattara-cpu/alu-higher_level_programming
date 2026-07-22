#!/usr/bin/python3
"""Module that defines a function to print text with indentation.

This module provides the text_indentation function, which prints a
text adding 2 new lines after each ., ? and : character.
"""


def text_indentation(text):
    """Print a text with 2 new lines after ., ? and :.

    Args:
        text (str): the text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
        elif char == "\n":
            print(line.strip())
            line = ""
    if line.strip():
        print(line.strip())
