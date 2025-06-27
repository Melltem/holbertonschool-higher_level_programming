#!/usr/bin/python3
"""BaseGeometry module."""

class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an exception for unimplemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer > 0."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
