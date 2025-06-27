#!/usr/bin/python3
"""Defines a class Student with attribute filtering in to_json."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.

        If attrs is a list of strings, return only those attributes.
        Otherwise, return all attributes.
        """
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
