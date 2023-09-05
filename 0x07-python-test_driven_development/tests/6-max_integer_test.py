#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 3, 4, 2]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 3, 4, 7]), 7)

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 4, -2]), 4)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 3, 4, 4, 2]), 4)

    def test_large_list(self):
        self.assertEqual(max_integer(list(range(1, 10001))), 10000)

if __name__ == '__main__':
    unittest.main()
