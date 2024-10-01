#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size: int = 0, position: tuple = (0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self) -> int:
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value: int):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self) -> tuple:
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value: tuple):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self) -> int:
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        # Print vertical spaces based on the position
        for _ in range(self.__position[1]):
            print("")

        # Print the square with the specified position
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self) -> str:
        """Return a string representation of the square."""
        if self.__size == 0:
            return ""
        
        lines = []
        for _ in range(self.__position[1]):
            lines.append("")  # Add empty lines for vertical position
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
