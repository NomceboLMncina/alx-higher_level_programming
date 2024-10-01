#!/usr/bin/python3
"""My square module"""


class Square:
    """Defines a square."""

    def __init__(self, size: int = 0):
        """Create a Square.
        Args:
            size: length of a side of Square.
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self) -> int:
        """The size of the Square's side.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self) -> int:
        """Get the area of the Square.
        Returns: The size squared.
        """
        return self.__size * self.__size

    def __le__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __lt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __ge__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()

    def __ne__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __gt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __eq__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __repr__(self) -> str:
        """Return a string representation of the Square."""
        return f"Square(size={self.size})"
