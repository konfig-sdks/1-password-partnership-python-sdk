import typing_extensions

from 1_password_partnership_python_sdk.apis.tags import TagValues
from 1_password_partnership_python_sdk.apis.tags.account_api import AccountApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNT: AccountApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNT: AccountApi,
    }
)
