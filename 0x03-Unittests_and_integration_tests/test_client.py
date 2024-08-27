#!/usr/bin/env python3
"""Unit tests for GithubOrgClient
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient
    """

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_data, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value
        """
        client = GithubOrgClient(org_name)
        mock_get_json.return_value = mock_data
        result = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, mock_data)


if __name__ == "__main__":
    unittest.main()
