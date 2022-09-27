#!/usr/bin/python3
"""``append_write`` module"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""

    n_appended = 0

    with open(filename, "a", encoding="utf-8") as f:
        n_appended = f.write(text)

    return n_appended
