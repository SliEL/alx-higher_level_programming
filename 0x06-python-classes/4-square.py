#!/usr/bin/python3

class Square:
    """Represent a square"""
    def __init__(self, size = 0) -> None:
        """Initialize a square
        Args:
            int (size): the size of the new square
        """
        self.__size = size
    
    @property
    def size(self):
        """retrieves the current size of the square"""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """sets a new size for the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)