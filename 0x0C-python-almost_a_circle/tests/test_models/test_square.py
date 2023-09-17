#!/usr/bin/python3

"""Module that defines unittests for square.py."""

import io
import sys
import unittest
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_str(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update_args(self):
        square = Square(5, 2, 3, 1)
        square.update(2, 4, 6, 8)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 8)
        self.assertEqual(square.id, 2)

    def test_update_kwargs(self):
        square = Square(5, 2, 3, 1)
        square.update(id=2, size=4, x=6, y=8)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 8)
        self.assertEqual(square.id, 2)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()