# coding: utf-8

"""
    1Password Partnership API

    Trusted by more than 100,000 businesses to protect their data, 1Password gives you complete control over passwords and other sensitive business information.   As an integral layer of the Identity and Access Management (IAM) stack, 1Password protects all employee accounts – even those you aren't aware of. Give employees secure access to any app or service and safely share everything you need to work together – including logins, documents, credit cards, and more – while keeping everything else private.  1Password is easy to deploy and integrates with Azure AD, Okta, OneLogin, and Slack, so you can automatically provision employees using the systems you already trust. It's simple to manage and fits seamlessly into your team's workflow, so you can secure your business without compromising productivity.

    The version of the OpenAPI document: 2.0.0
    Contact: partners@1password.com
    Created by: https://www.1password.partners/English/
"""

import unittest
from 1_password_partnership_python_sdk.configuration import check_url
from 1_password_partnership_python_sdk.exceptions import InvalidHostConfigurationError


class TestIsValidUrl(unittest.TestCase):
    def test_valid_urls(self):
        valid_urls = [
            "http://www.example.com",
            "https://www.example.com",
            "http://example.com",
            "https://example.com/path/to/resource",
            "http://example.com:8080",
            "https://example.co.uk",
            "https://subdomain.example.com",
            "https://api.example.com/v1/resource",
            "https://example.com/path/to/resource/123",
            "https://www.example.com:8080",
            "https://www.example.com:8080/path/to/resource",
            "http://sub.example.com:8080",
            "http://deep.sub.domain.example.com",
            "http://127.0.0.1:4010",
            "https://deep.sub.domain.example.com:8080/path",
            "http://example.io",
            "https://example.app",
        ]
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(check_url(url))

    def test_invalid_urls(self):
        invalid_urls = [
            "not_a_url",
            "http:/example.com",
            "http://",
            "http://.com",
            "example.com",
            "http://example.com#fragment",
            "www.example.com",
            "https://example.com/path/to/resource?query=value",
            "https://example.com/path/to/resource?query=value&key2=value2",
            "https://",
            "ftp://files.example.com",
            "//example.com",
            "https://example,com",
            "https:/example.com",
            "https:// example.com",
            "https://example.com path",
            "http://..com",
            "https://..example.com",
            "http://example..com",
            "https://example.com./path",
            "https://example.com..",
            "http://:8080",
            "https://example.com:",
            "http://example.com:abc",
            "https://.example.com",
            "http://example.",
            "https:// example:8080.com",
            "http:// example.com:8080/path",
            "https://:8080/path",
        ]
        for url in invalid_urls:
            with self.subTest(url=url):
                with self.assertRaises(InvalidHostConfigurationError):
                    check_url(url)
                    raise Exception("URL should be invalid: " + url)


if __name__ == "__main__":
    unittest.main()
