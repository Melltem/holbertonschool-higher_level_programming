#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception indicating the area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer or is a bool.
            ValueError: If value is <= 0.
        """
        # Check if value is int but exclude bool (since bool is subclass of int)
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
