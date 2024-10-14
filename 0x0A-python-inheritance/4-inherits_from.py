#!/usr/bin/python3
"""
===================================
module with method inherits_from
===================================
"""

def inherits_from(obj, a_class):
    """Method that returns True if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a_class's subclass; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
