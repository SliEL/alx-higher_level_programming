#!/usr/bin/python3

class Square:
    """Represents a square"""
    
    def __init__(self, size = 0):
        """Initialize the square
        Args: 
            size (int): the size of the new square
        """
        self.size = size

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
        """returns the area of the square"""
        return (self.__size * self.__size)
    
    def my_print(self):
        """prints the size of the square"""
        for _  in range(0, self.__size):
            [print("#", end="") for _ in range(0, self.__size)]
            print("")
        if (self.__size == 0):
            print("")

    