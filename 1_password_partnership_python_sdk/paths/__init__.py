# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from 1_password_partnership_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V1_PARTNERS_ACCOUNTS = "/api/v1/partners/accounts"
    API_V1_PARTNERS_ACCOUNTS_CUSTOMER_ACCOUNT_UID = "/api/v1/partners/accounts/{customer_account_uid}"
