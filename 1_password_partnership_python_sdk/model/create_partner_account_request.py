# coding: utf-8

"""
    1Password Partnership API

    Trusted by more than 100,000 businesses to protect their data, 1Password gives you complete control over passwords and other sensitive business information.   As an integral layer of the Identity and Access Management (IAM) stack, 1Password protects all employee accounts – even those you aren't aware of. Give employees secure access to any app or service and safely share everything you need to work together – including logins, documents, credit cards, and more – while keeping everything else private.  1Password is easy to deploy and integrates with Azure AD, Okta, OneLogin, and Slack, so you can automatically provision employees using the systems you already trust. It's simple to manage and fits seamlessly into your team's workflow, so you can secure your business without compromising productivity.

    The version of the OpenAPI document: 2.0.0
    Contact: partners@1password.com
    Created by: https://www.1password.partners/English/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from 1_password_partnership_python_sdk import schemas  # noqa: F401


class CreatePartnerAccountRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "customer_account_uid",
            "account_type",
            "domain",
        }
        
        class properties:
            customer_account_uid = schemas.StrSchema
            account_type = schemas.StrSchema
            domain = schemas.StrSchema
            ends_at = schemas.DateTimeSchema
            __annotations__ = {
                "customer_account_uid": customer_account_uid,
                "account_type": account_type,
                "domain": domain,
                "ends_at": ends_at,
            }
    
    customer_account_uid: MetaOapg.properties.customer_account_uid
    account_type: MetaOapg.properties.account_type
    domain: MetaOapg.properties.domain
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer_account_uid"]) -> MetaOapg.properties.customer_account_uid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_type"]) -> MetaOapg.properties.account_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ends_at"]) -> MetaOapg.properties.ends_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customer_account_uid", "account_type", "domain", "ends_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer_account_uid"]) -> MetaOapg.properties.customer_account_uid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_type"]) -> MetaOapg.properties.account_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ends_at"]) -> typing.Union[MetaOapg.properties.ends_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customer_account_uid", "account_type", "domain", "ends_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        customer_account_uid: typing.Union[MetaOapg.properties.customer_account_uid, str, ],
        account_type: typing.Union[MetaOapg.properties.account_type, str, ],
        domain: typing.Union[MetaOapg.properties.domain, str, ],
        ends_at: typing.Union[MetaOapg.properties.ends_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreatePartnerAccountRequest':
        return super().__new__(
            cls,
            *args,
            customer_account_uid=customer_account_uid,
            account_type=account_type,
            domain=domain,
            ends_at=ends_at,
            _configuration=_configuration,
            **kwargs,
        )
