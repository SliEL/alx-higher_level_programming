#!/usr/bin/python3

"""Module that defines unittests for models/rectangle.py."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_init_with_valid_args(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_init_with_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_init_with_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 0)

    def test_init_with_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 5, -1)

    def test_init_with_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 5, 1, -2)

    def test_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_display(self):
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update_args(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        rect.update(20, 6, 7, 3, 4)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_kwargs(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        rect.update(id=20, width=6, height=7, x=3, y=4)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        expected_dict = {
            "id": 10,
            "width": 4,
            "height": 5,
            "x": 1,
            "y": 2
        }
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_str(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        expected_str = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(rect), expected_str)

if __name__ == '__main__':
    unittest.main()