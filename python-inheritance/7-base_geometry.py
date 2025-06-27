#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class with basic methods."""

    def area(self):
        """Raise an Exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
