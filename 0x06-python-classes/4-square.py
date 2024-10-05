#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size: int = 0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size  # Using the setter for validation

    @property
    def size(self) -> int:
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value: int):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """Return the current area of the square."""
        return self.__size * self.__size

    def __str__(self) -> str:
        """Return a string representation of the square."""
        return f"Square with size {self.__size}"