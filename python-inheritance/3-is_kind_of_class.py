#!/usr/bin/python3
"""Return True if obj is an instance of a_class or its subclass, else False."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass, else False."""
    return isinstance(obj, a_class)
