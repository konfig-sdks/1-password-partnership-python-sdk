# coding: utf-8

# flake8: noqa

"""
    1Password Partnership API

    Trusted by more than 100,000 businesses to protect their data, 1Password gives you complete control over passwords and other sensitive business information.   As an integral layer of the Identity and Access Management (IAM) stack, 1Password protects all employee accounts – even those you aren't aware of. Give employees secure access to any app or service and safely share everything you need to work together – including logins, documents, credit cards, and more – while keeping everything else private.  1Password is easy to deploy and integrates with Azure AD, Okta, OneLogin, and Slack, so you can automatically provision employees using the systems you already trust. It's simple to manage and fits seamlessly into your team's workflow, so you can secure your business without compromising productivity.

    The version of the OpenAPI document: 2.0.0
    Contact: partners@1password.com
    Created by: https://www.1password.partners/English/
"""

__version__ = "2.0.0"

# import ApiClient
from 1_password_partnership_python_sdk.api_client import ApiClient

# import Configuration
from 1_password_partnership_python_sdk.configuration import Configuration

# import exceptions
from 1_password_partnership_python_sdk.exceptions import OpenApiException
from 1_password_partnership_python_sdk.exceptions import ApiAttributeError
from 1_password_partnership_python_sdk.exceptions import ApiTypeError
from 1_password_partnership_python_sdk.exceptions import ApiValueError
from 1_password_partnership_python_sdk.exceptions import ApiKeyError
from 1_password_partnership_python_sdk.exceptions import ApiException

from 1_password_partnership_python_sdk.client import OnePasswordPartnership
