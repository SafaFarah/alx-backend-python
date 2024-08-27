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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repos
        """
        mock_repos_payload = [
            {"id": 7697149, "name": "alx_python", "private": False},
            {"id": 8566972, "name": "back_end", "private": False}
        ]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as moc_repo_url:
            moc_repo_url.return_value = "https://api.github.com/orgs/ABC/repos"
            mock_get_json.return_value = mock_repos_payload
            client = GithubOrgClient("ABC")
            repos = client.public_repos()
            expected_repos = ["alx_python", "back_end"]
            self.assertEqual(repos, expected_repos)
            moc_repo_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license correctly identifies the presence of a license
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
