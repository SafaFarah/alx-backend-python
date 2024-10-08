#!/usr/bin/env python3
"""Unit tests for utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """Test case for get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json function with mocked requests.get
        """
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for memoize decorator
    """

    def test_memoize(self):
        """Test that memoize correctly caches results
        """
        class TestClass:
            """Class to test memoize decorator
            """
            def a_method(self):
                """Method that will be mocked"""
                return 42

            @memoize
            def a_property(self):
                """Property that uses memoization"""
                return self.a_method()
        obj = TestClass()
        with patch.object(obj, 'a_method', return_value=42) as mock_method:
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
