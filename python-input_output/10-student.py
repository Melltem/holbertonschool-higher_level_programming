#!/usr/bin/python3
"""Retrieve dictionary representation of Student."""


def to_json(self, attrs=None):
    """Retrieve dictionary representation of Student.

    If attrs is a list of strings, return only those attributes.
    Otherwise, return all attributes.
    """
    if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
        return {
            key: getattr(self, key)
            for key in attrs
            if hasattr(self, key)
        }
    return self.__dict__
