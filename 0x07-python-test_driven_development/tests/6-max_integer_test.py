#!/usr/bin/python3
"""Unittests for max_integer([...])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([...])."""

    def test_sorted_list(self):
        """Test an sorted list of integers."""
        sorted_list = [1, 2, 3, 4, 5, 100]
        self.assertEqual(max_integer(sorted_list), 100)

    def test_unsorted_list(self):
        """Test an unsorted list of integers."""
        unsorted_list = [200, 1, 2, 4, 3]
        self.assertEqual(max_integer(unsorted_list), 200)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [2_000_000]
        self.assertEqual(max_integer(one_element), 2_000_000)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 5.33, -9.5123, 20.25, 6.0]
        self.assertEqual(max_integer(floats), 20.25)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [15.5, -8, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "ALX"
        self.assertEqual(max_integer(string), 'X')


if __name__ == "__main__":
    unittest.main()
