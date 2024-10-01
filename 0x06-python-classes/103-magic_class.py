#!/usr/bin/python3
"""Magic class from a given ByteCode."""
import math


class MagicClass:
    """Initialization of the MagicClass."""

    def __init__(self, radius: float = 0):
        """Initialize the MagicClass with a radius.
        
        Args:
            radius (float): The radius of the circle.
        
        Raises:
            TypeError: If radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle.
        
        Returns:
            float: The area of the circle.
        """
        return self.radius ** 2 * math.pi

    def circumference(self) -> float:
        """Calculate the circumference of the circle.
        
        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.radius
