# coding: utf-8

"""
    1Password Partnership API

    Trusted by more than 100,000 businesses to protect their data, 1Password gives you complete control over passwords and other sensitive business information.   As an integral layer of the Identity and Access Management (IAM) stack, 1Password protects all employee accounts – even those you aren't aware of. Give employees secure access to any app or service and safely share everything you need to work together – including logins, documents, credit cards, and more – while keeping everything else private.  1Password is easy to deploy and integrates with Azure AD, Okta, OneLogin, and Slack, so you can automatically provision employees using the systems you already trust. It's simple to manage and fits seamlessly into your team's workflow, so you can secure your business without compromising productivity.

    The version of the OpenAPI document: 2.0.0
    Contact: partners@1password.com
    Created by: https://www.1password.partners/English/
"""

import unittest
from unittest.mock import patch

import urllib3

import 1_password_partnership_python_sdk
from 1_password_partnership_python_sdk.paths.api_v1_partners_accounts import post
from 1_password_partnership_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1PartnersAccounts(ApiTestMixin, unittest.TestCase):
    """
    ApiV1PartnersAccounts unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201






if __name__ == '__main__':
    unittest.main()
