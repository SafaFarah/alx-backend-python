#!/usr/bin/env python3
"""Unit tests for utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function with various inputs
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"], "'a'"),
        ({"a": 1}, ["a", "b"], "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, exp_message):
        """Test access_nested_map function raises KeyError for invalid paths
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), exp_message)


if __name__ == "__main__":
    unittest.main()
