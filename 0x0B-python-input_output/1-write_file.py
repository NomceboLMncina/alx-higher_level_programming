#!/usr/bin/python3
"""Defines a file-writing function."""

def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.

    Args:
        filename (str): The name of the file to write. If it
        does not exist, it will be created.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            return f.write(text)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
        return 0
