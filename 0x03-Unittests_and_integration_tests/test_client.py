#!/usr/bin/env python3
"""Unit tests for GithubOrgClient
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
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


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient
    """

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL
        """
        client = GithubOrgClient("ABC")
        mock_org_data = {
            "repos_url": "https://api.github.com/orgs/ABC/repos"
        }
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = mock_org_data
            self.assertEqual(client._public_repos_url,
                             "https://api.github.com/orgs/ABC/repos")


if __name__ == "__main__":
    unittest.main()
