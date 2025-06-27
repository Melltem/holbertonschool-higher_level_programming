#!/usr/bin/python3
"""Module to check if an object inherits from a specified class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherits from a_class, else False."""
    # Check if obj's class is a subclass of a_class but not the class itself
    return issubclass(type(obj), a_class) and type(obj) is not a_class
