# coding: utf-8

"""
    1Password Partnership API

    Trusted by more than 100,000 businesses to protect their data, 1Password gives you complete control over passwords and other sensitive business information.   As an integral layer of the Identity and Access Management (IAM) stack, 1Password protects all employee accounts – even those you aren't aware of. Give employees secure access to any app or service and safely share everything you need to work together – including logins, documents, credit cards, and more – while keeping everything else private.  1Password is easy to deploy and integrates with Azure AD, Okta, OneLogin, and Slack, so you can automatically provision employees using the systems you already trust. It's simple to manage and fits seamlessly into your team's workflow, so you can secure your business without compromising productivity.

    The version of the OpenAPI document: 2.0.0
    Contact: partners@1password.com
    Created by: https://www.1password.partners/English/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredAccount(TypedDict):
    pass

class OptionalAccount(TypedDict, total=False):
    # The unique identifier for the end user's account. It can be up to 80 chars long and consist of alphanumeric characters and hyphens.
    customer_account_uid: str

    # The current type of the 1Password account - 'I' for Individual, or 'F' for family.
    account_type: str

    # The activation token is a coupon code to link a new or existing 1Password account to a partnership promotion. For example, it can be used for 1Password account creation at https://start.{{1password_domain}}/partnership/redeem?t={{account_type}}&c={{activation_token}} during end-user signup.
    activation_token: str

    # The 1Password domain for which the account was provisioned for. For testing domains, it can be one of 'b5test.com', 'b5test.ca', or 'b5test.eu'. For production, it can be one of '1password.com', '1password.ca', or '1password.eu'.
    domain: str

    # The provisioning status of the partner account. It can be either 'entitled' for accounts that have been initialized but have not completed 1Password signup, or 'provisioned' for accounts that have completed the 1Password signup process.
    status: str

    # The number of provisioned users for the 1Password account.
    deployed_members: int

    # The timestamp of when the partnership account was created, formatted in RFC-3339.
    created_at: datetime

    # The timestamp of when the partner account was last updated, formatted in RFC-3339. This field will be updated during account status changes.
    updated_at: datetime

    # The timestamp of when the partner account will be frozen, formatted in RFC-3339.
    ends_at: datetime

class Account(RequiredAccount, OptionalAccount):
    pass
