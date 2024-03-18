import typing_extensions

from 1_password_partnership_python_sdk.paths import PathValues
from 1_password_partnership_python_sdk.apis.paths.api_v1_partners_accounts import ApiV1PartnersAccounts
from 1_password_partnership_python_sdk.apis.paths.api_v1_partners_accounts_customer_account_uid import ApiV1PartnersAccountsCustomerAccountUid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_PARTNERS_ACCOUNTS: ApiV1PartnersAccounts,
        PathValues.API_V1_PARTNERS_ACCOUNTS_CUSTOMER_ACCOUNT_UID: ApiV1PartnersAccountsCustomerAccountUid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_PARTNERS_ACCOUNTS: ApiV1PartnersAccounts,
        PathValues.API_V1_PARTNERS_ACCOUNTS_CUSTOMER_ACCOUNT_UID: ApiV1PartnersAccountsCustomerAccountUid,
    }
)
