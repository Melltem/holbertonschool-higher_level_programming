#!/usr/bin/python3
"""Square class inherits from Rectangle."""

Rectangle = __import__('8-rectangle').Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with size.

        Size must be validated as a positive integer using integer_validator.
        """
        self.integer_validator("size", size)
        self.__size = size
        # Initialize the parent Rectangle with width and height equal to size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
