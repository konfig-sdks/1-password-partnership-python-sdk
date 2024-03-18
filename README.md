<div align="left">

[![Visit 1password](./header.png)](https://1password.com)

# 1password<a id="1password"></a>

Trusted by more than 100,000 businesses to protect their data, 1Password gives you complete control over passwords and other sensitive business information. 

As an integral layer of the Identity and Access Management (IAM) stack, 1Password protects all employee accounts – even those you aren't aware of. Give employees secure access to any app or service and safely share everything you need to work together – including logins, documents, credit cards, and more – while keeping everything else private.

1Password is easy to deploy and integrates with Azure AD, Okta, OneLogin, and Slack, so you can automatically provision employees using the systems you already trust. It's simple to manage and fits seamlessly into your team's workflow, so you can secure your business without compromising productivity.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`onepasswordpartnership.account.begin_provisioning_process`](#onepasswordpartnershipaccountbegin_provisioning_process)
  * [`onepasswordpartnership.account.get_by_uid`](#onepasswordpartnershipaccountget_by_uid)
  * [`onepasswordpartnership.account.remove_from_partnership`](#onepasswordpartnershipaccountremove_from_partnership)
  * [`onepasswordpartnership.account.update_ends_at_by_uid`](#onepasswordpartnershipaccountupdate_ends_at_by_uid)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=1Password&serviceName=Partnership&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from 1_password_partnership_python_sdk import OnePasswordPartnership, ApiException

onepasswordpartnership = OnePasswordPartnership(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    begin_provisioning_process_response = onepasswordpartnership.account.begin_provisioning_process(
        customer_account_uid="string_example",
        account_type="string_example",
        domain="string_example",
        ends_at="1970-01-01T00:00:00.00Z",
    )
    print(begin_provisioning_process_response)
except ApiException as e:
    print("Exception when calling AccountApi.begin_provisioning_process: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["description"])
        pprint(e.body["code"])
        pprint(e.body["error"])
    if e.status == 500:
        pprint(e.body["description"])
        pprint(e.body["code"])
        pprint(e.body["error"])
    if e.status == 403:
        pprint(e.body["description"])
        pprint(e.body["code"])
        pprint(e.body["error"])
    if e.status == 404:
        pprint(e.body["description"])
        pprint(e.body["code"])
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from 1_password_partnership_python_sdk import OnePasswordPartnership, ApiException

onepasswordpartnership = OnePasswordPartnership(

    access_token = 'YOUR_BEARER_TOKEN'
)

async def main():
    try:
        begin_provisioning_process_response = await onepasswordpartnership.account.abegin_provisioning_process(
            customer_account_uid="string_example",
            account_type="string_example",
            domain="string_example",
            ends_at="1970-01-01T00:00:00.00Z",
        )
        print(begin_provisioning_process_response)
    except ApiException as e:
        print("Exception when calling AccountApi.begin_provisioning_process: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["description"])
            pprint(e.body["code"])
            pprint(e.body["error"])
        if e.status == 500:
            pprint(e.body["description"])
            pprint(e.body["code"])
            pprint(e.body["error"])
        if e.status == 403:
            pprint(e.body["description"])
            pprint(e.body["code"])
            pprint(e.body["error"])
        if e.status == 404:
            pprint(e.body["description"])
            pprint(e.body["code"])
            pprint(e.body["error"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from 1_password_partnership_python_sdk import OnePasswordPartnership, ApiException

onepasswordpartnership = OnePasswordPartnership(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    begin_provisioning_process_response = onepasswordpartnership.account.raw.begin_provisioning_process(
        customer_account_uid="string_example",
        account_type="string_example",
        domain="string_example",
        ends_at="1970-01-01T00:00:00.00Z",
    )
    pprint(begin_provisioning_process_response.body)
    pprint(begin_provisioning_process_response.body["customer_account_uid"])
    pprint(begin_provisioning_process_response.body["account_type"])
    pprint(begin_provisioning_process_response.body["activation_token"])
    pprint(begin_provisioning_process_response.body["domain"])
    pprint(begin_provisioning_process_response.body["status"])
    pprint(begin_provisioning_process_response.body["deployed_members"])
    pprint(begin_provisioning_process_response.body["created_at"])
    pprint(begin_provisioning_process_response.body["updated_at"])
    pprint(begin_provisioning_process_response.body["ends_at"])
    pprint(begin_provisioning_process_response.headers)
    pprint(begin_provisioning_process_response.status)
    pprint(begin_provisioning_process_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountApi.begin_provisioning_process: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["description"])
        pprint(e.body["code"])
        pprint(e.body["error"])
    if e.status == 500:
        pprint(e.body["description"])
        pprint(e.body["code"])
        pprint(e.body["error"])
    if e.status == 403:
        pprint(e.body["description"])
        pprint(e.body["code"])
        pprint(e.body["error"])
    if e.status == 404:
        pprint(e.body["description"])
        pprint(e.body["code"])
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `onepasswordpartnership.account.begin_provisioning_process`<a id="onepasswordpartnershipaccountbegin_provisioning_process"></a>

Begins provisioning process for a new partner associated 1Password account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
begin_provisioning_process_response = onepasswordpartnership.account.begin_provisioning_process(
    customer_account_uid="string_example",
    account_type="string_example",
    domain="string_example",
    ends_at="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_account_uid: `str`<a id="customer_account_uid-str"></a>

A unique identifier for the end user's account to be provisioned. It can be up to 80 chars long and consist of alphanumeric characters and hyphens.

##### account_type: `str`<a id="account_type-str"></a>

Specifies the type of 1Password account plan to provision - 'I' for Individual, or 'F' for family.

##### domain: `str`<a id="domain-str"></a>

Specifies the 1Password domain to provision the account for. For testing it can be one of 'b5test.com', 'b5test.ca', or 'b5test.eu'. For production, it can be one of '1password.com', '1password.ca', or '1password.eu'. Note that domains can only be used after promotions have been created for a given partnership in the specific domain.

##### ends_at: `datetime`<a id="ends_at-datetime"></a>

Specifies when the 1Password account will be frozen, formatted in RFC-3339.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreatePartnerAccountRequest`](./1_password_partnership_python_sdk/type/create_partner_account_request.py)
Request to initialize a partner account.

#### 🔄 Return<a id="🔄-return"></a>

[`Account`](./1_password_partnership_python_sdk/pydantic/account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/partners/accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `onepasswordpartnership.account.get_by_uid`<a id="onepasswordpartnershipaccountget_by_uid"></a>

Returns an account based on an UID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_uid_response = onepasswordpartnership.account.get_by_uid(
    customer_account_uid="customer_account_uid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_account_uid: `str`<a id="customer_account_uid-str"></a>

Unique ID of an account to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`Account`](./1_password_partnership_python_sdk/pydantic/account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/partners/accounts/{customer_account_uid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `onepasswordpartnership.account.remove_from_partnership`<a id="onepasswordpartnershipaccountremove_from_partnership"></a>

Removes an account from the partnership domain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
onepasswordpartnership.account.remove_from_partnership(
    customer_account_uid="customer_account_uid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_account_uid: `str`<a id="customer_account_uid-str"></a>

Unique ID of partner_account to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/partners/accounts/{customer_account_uid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `onepasswordpartnership.account.update_ends_at_by_uid`<a id="onepasswordpartnershipaccountupdate_ends_at_by_uid"></a>

Updates the ends_at attribute of an account based on an UID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_ends_at_by_uid_response = onepasswordpartnership.account.update_ends_at_by_uid(
    ends_at="1970-01-01T00:00:00.00Z",
    customer_account_uid="customer_account_uid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ends_at: `datetime`<a id="ends_at-datetime"></a>

Specifies when the 1Password account will be frozen, formatted in RFC-3339.

##### customer_account_uid: `str`<a id="customer_account_uid-str"></a>

Unique ID of partner_account to update.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdatePartnerAccountRequest`](./1_password_partnership_python_sdk/type/update_partner_account_request.py)
Request to update the ends_at attribute of a partner account.

#### 🔄 Return<a id="🔄-return"></a>

[`Account`](./1_password_partnership_python_sdk/pydantic/account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/partners/accounts/{customer_account_uid}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
