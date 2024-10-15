#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json

def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        """Return the Python object representation of a JSON string."""
        return json.load(f)
