#!/usr/bin/python3
"""module that defines unittests for base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string_empty(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_non_empty(self):
        data = [{"key": "value"}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"key": "value"}]')

    def test_from_json_string_empty(self):
        data = Base.from_json_string("[]")
        self.assertEqual(data, [])

    def test_from_json_string_non_empty(self):
        json_str = '[{"key": "value"}]'
        data = Base.from_json_string(json_str)
        self.assertEqual(data, [{"key": "value"}])

    def test_create(self):
        dictionary = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 1)

    def test_save_to_file(self):
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file([obj1, obj2])
        # You can add code to check if the file was created and contains the expected JSON data.

    def test_load_from_file(self):
        # You can add code to create a test JSON file, save some data, and then test if it can be loaded correctly.
        pass

    # Add more tests for other methods like save_to_file_csv, load_from_file_csv, and draw.

if __name__ == '__main__':
    unittest.main()