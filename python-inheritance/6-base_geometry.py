#!/usr/bin/python3
"""Defines class BaseGeometry with
an unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an exception for
        unimplemented area method."""
        raise Exception("area() is not implemented")
