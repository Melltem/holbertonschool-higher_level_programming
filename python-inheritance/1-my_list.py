#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""


class MyList(list):
    """A class that inherits from list and can print a sorted version."""

    def print_sorted(self):
        """Print the list, sorted in ascending order."""
        print(sorted(self))
