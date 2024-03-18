# coding: utf-8

"""
    1Password Partnership API

    Trusted by more than 100,000 businesses to protect their data, 1Password gives you complete control over passwords and other sensitive business information.   As an integral layer of the Identity and Access Management (IAM) stack, 1Password protects all employee accounts – even those you aren't aware of. Give employees secure access to any app or service and safely share everything you need to work together – including logins, documents, credit cards, and more – while keeping everything else private.  1Password is easy to deploy and integrates with Azure AD, Okta, OneLogin, and Slack, so you can automatically provision employees using the systems you already trust. It's simple to manage and fits seamlessly into your team's workflow, so you can secure your business without compromising productivity.

    The version of the OpenAPI document: 2.0.0
    Contact: partners@1password.com
    Created by: https://www.1password.partners/English/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from 1_password_partnership_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from 1_password_partnership_python_sdk.api_response import AsyncGeneratorResponse
from 1_password_partnership_python_sdk import api_client, exceptions
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

from 1_password_partnership_python_sdk.model.error import Error as ErrorSchema
from 1_password_partnership_python_sdk.model.create_partner_account_request import CreatePartnerAccountRequest as CreatePartnerAccountRequestSchema
from 1_password_partnership_python_sdk.model.account import Account as AccountSchema

from 1_password_partnership_python_sdk.type.create_partner_account_request import CreatePartnerAccountRequest
from 1_password_partnership_python_sdk.type.error import Error
from 1_password_partnership_python_sdk.type.account import Account

from ...api_client import Dictionary
from 1_password_partnership_python_sdk.pydantic.error import Error as ErrorPydantic
from 1_password_partnership_python_sdk.pydantic.create_partner_account_request import CreatePartnerAccountRequest as CreatePartnerAccountRequestPydantic
from 1_password_partnership_python_sdk.pydantic.account import Account as AccountPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CreatePartnerAccountRequestSchema


request_body_create_partner_account_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'bearerAuth',
]
LocationSchema = schemas.StrSchema
location_parameter = api_client.HeaderParameter(
    name="location",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LocationSchema,
)
SchemaFor201ResponseBodyApplicationJson = AccountSchema
ResponseHeadersFor201 = typing_extensions.TypedDict(
    'ResponseHeadersFor201',
    {
        'location': LocationSchema,
    }
)


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Account


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Account


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
    headers=[
        location_parameter,
    ]
)
SchemaFor400ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Error


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: Error


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: Error


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: Error


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '403': _response_for_403,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _begin_provisioning_process_mapped_args(
        self,
        customer_account_uid: str,
        account_type: str,
        domain: str,
        ends_at: typing.Optional[datetime] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if customer_account_uid is not None:
            _body["customer_account_uid"] = customer_account_uid
        if account_type is not None:
            _body["account_type"] = account_type
        if domain is not None:
            _body["domain"] = domain
        if ends_at is not None:
            _body["ends_at"] = ends_at
        args.body = _body
        return args

    async def _abegin_provisioning_process_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/partners/accounts',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_partner_account_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _begin_provisioning_process_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/partners/accounts',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_partner_account_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class BeginProvisioningProcessRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def abegin_provisioning_process(
        self,
        customer_account_uid: str,
        account_type: str,
        domain: str,
        ends_at: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._begin_provisioning_process_mapped_args(
            customer_account_uid=customer_account_uid,
            account_type=account_type,
            domain=domain,
            ends_at=ends_at,
        )
        return await self._abegin_provisioning_process_oapg(
            body=args.body,
            **kwargs,
        )
    
    def begin_provisioning_process(
        self,
        customer_account_uid: str,
        account_type: str,
        domain: str,
        ends_at: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._begin_provisioning_process_mapped_args(
            customer_account_uid=customer_account_uid,
            account_type=account_type,
            domain=domain,
            ends_at=ends_at,
        )
        return self._begin_provisioning_process_oapg(
            body=args.body,
        )

class BeginProvisioningProcess(BaseApi):

    async def abegin_provisioning_process(
        self,
        customer_account_uid: str,
        account_type: str,
        domain: str,
        ends_at: typing.Optional[datetime] = None,
        validate: bool = False,
        **kwargs,
    ) -> AccountPydantic:
        raw_response = await self.raw.abegin_provisioning_process(
            customer_account_uid=customer_account_uid,
            account_type=account_type,
            domain=domain,
            ends_at=ends_at,
            **kwargs,
        )
        if validate:
            return AccountPydantic(**raw_response.body)
        return api_client.construct_model_instance(AccountPydantic, raw_response.body)
    
    
    def begin_provisioning_process(
        self,
        customer_account_uid: str,
        account_type: str,
        domain: str,
        ends_at: typing.Optional[datetime] = None,
        validate: bool = False,
    ) -> AccountPydantic:
        raw_response = self.raw.begin_provisioning_process(
            customer_account_uid=customer_account_uid,
            account_type=account_type,
            domain=domain,
            ends_at=ends_at,
        )
        if validate:
            return AccountPydantic(**raw_response.body)
        return api_client.construct_model_instance(AccountPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        customer_account_uid: str,
        account_type: str,
        domain: str,
        ends_at: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._begin_provisioning_process_mapped_args(
            customer_account_uid=customer_account_uid,
            account_type=account_type,
            domain=domain,
            ends_at=ends_at,
        )
        return await self._abegin_provisioning_process_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        customer_account_uid: str,
        account_type: str,
        domain: str,
        ends_at: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._begin_provisioning_process_mapped_args(
            customer_account_uid=customer_account_uid,
            account_type=account_type,
            domain=domain,
            ends_at=ends_at,
        )
        return self._begin_provisioning_process_oapg(
            body=args.body,
        )

