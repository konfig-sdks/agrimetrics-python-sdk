# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from agrimetrics_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from agrimetrics_python_sdk.api_response import AsyncGeneratorResponse
from agrimetrics_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from agrimetrics_python_sdk import schemas  # noqa: F401

from agrimetrics_python_sdk.model.batch_identity_input_entitlements import BatchIdentityInputEntitlements as BatchIdentityInputEntitlementsSchema
from agrimetrics_python_sdk.model.exchange import Exchange as ExchangeSchema
from agrimetrics_python_sdk.model.data_set_template_metadata import DataSetTemplateMetadata as DataSetTemplateMetadataSchema
from agrimetrics_python_sdk.model.entry_update_response import EntryUpdateResponse as EntryUpdateResponseSchema
from agrimetrics_python_sdk.model.data_set_patch import DataSetPatch as DataSetPatchSchema
from agrimetrics_python_sdk.model.entitlements import Entitlements as EntitlementsSchema

from agrimetrics_python_sdk.type.entitlements import Entitlements
from agrimetrics_python_sdk.type.entry_update_response import EntryUpdateResponse
from agrimetrics_python_sdk.type.exchange import Exchange
from agrimetrics_python_sdk.type.data_set_template_metadata import DataSetTemplateMetadata
from agrimetrics_python_sdk.type.data_set_patch import DataSetPatch
from agrimetrics_python_sdk.type.batch_identity_input_entitlements import BatchIdentityInputEntitlements

from ...api_client import Dictionary
from agrimetrics_python_sdk.pydantic.data_set_patch import DataSetPatch as DataSetPatchPydantic
from agrimetrics_python_sdk.pydantic.batch_identity_input_entitlements import BatchIdentityInputEntitlements as BatchIdentityInputEntitlementsPydantic
from agrimetrics_python_sdk.pydantic.entry_update_response import EntryUpdateResponse as EntryUpdateResponsePydantic
from agrimetrics_python_sdk.pydantic.data_set_template_metadata import DataSetTemplateMetadata as DataSetTemplateMetadataPydantic
from agrimetrics_python_sdk.pydantic.exchange import Exchange as ExchangePydantic
from agrimetrics_python_sdk.pydantic.entitlements import Entitlements as EntitlementsPydantic

# body param
SchemaForRequestBodyApplicationJson = DataSetTemplateMetadataSchema


request_body_data_set_template_metadata = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = EntryUpdateResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: EntryUpdateResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: EntryUpdateResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_catalog_entry_mapped_args(
        self,
        name: str,
        description: typing.Optional[str] = None,
        data_set: typing.Optional[DataSetPatch] = None,
        entitlements: typing.Optional[BatchIdentityInputEntitlements] = None,
        creator_entitlements: typing.Optional[Entitlements] = None,
        exchange: typing.Optional[Exchange] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if data_set is not None:
            _body["dataSet"] = data_set
        if entitlements is not None:
            _body["entitlements"] = entitlements
        if creator_entitlements is not None:
            _body["creatorEntitlements"] = creator_entitlements
        if exchange is not None:
            _body["exchange"] = exchange
        args.body = _body
        return args

    async def _acreate_catalog_entry_oapg(
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
        Create a new template for creating catalogue entries.
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/templates',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_data_set_template_metadata.serialize(body, content_type)
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


    def _create_catalog_entry_oapg(
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
        Create a new template for creating catalogue entries.
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/templates',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_data_set_template_metadata.serialize(body, content_type)
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


class CreateCatalogEntryRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_catalog_entry(
        self,
        name: str,
        description: typing.Optional[str] = None,
        data_set: typing.Optional[DataSetPatch] = None,
        entitlements: typing.Optional[BatchIdentityInputEntitlements] = None,
        creator_entitlements: typing.Optional[Entitlements] = None,
        exchange: typing.Optional[Exchange] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_catalog_entry_mapped_args(
            name=name,
            description=description,
            data_set=data_set,
            entitlements=entitlements,
            creator_entitlements=creator_entitlements,
            exchange=exchange,
        )
        return await self._acreate_catalog_entry_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_catalog_entry(
        self,
        name: str,
        description: typing.Optional[str] = None,
        data_set: typing.Optional[DataSetPatch] = None,
        entitlements: typing.Optional[BatchIdentityInputEntitlements] = None,
        creator_entitlements: typing.Optional[Entitlements] = None,
        exchange: typing.Optional[Exchange] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_catalog_entry_mapped_args(
            name=name,
            description=description,
            data_set=data_set,
            entitlements=entitlements,
            creator_entitlements=creator_entitlements,
            exchange=exchange,
        )
        return self._create_catalog_entry_oapg(
            body=args.body,
        )

class CreateCatalogEntry(BaseApi):

    async def acreate_catalog_entry(
        self,
        name: str,
        description: typing.Optional[str] = None,
        data_set: typing.Optional[DataSetPatch] = None,
        entitlements: typing.Optional[BatchIdentityInputEntitlements] = None,
        creator_entitlements: typing.Optional[Entitlements] = None,
        exchange: typing.Optional[Exchange] = None,
        validate: bool = False,
        **kwargs,
    ) -> EntryUpdateResponsePydantic:
        raw_response = await self.raw.acreate_catalog_entry(
            name=name,
            description=description,
            data_set=data_set,
            entitlements=entitlements,
            creator_entitlements=creator_entitlements,
            exchange=exchange,
            **kwargs,
        )
        if validate:
            return EntryUpdateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EntryUpdateResponsePydantic, raw_response.body)
    
    
    def create_catalog_entry(
        self,
        name: str,
        description: typing.Optional[str] = None,
        data_set: typing.Optional[DataSetPatch] = None,
        entitlements: typing.Optional[BatchIdentityInputEntitlements] = None,
        creator_entitlements: typing.Optional[Entitlements] = None,
        exchange: typing.Optional[Exchange] = None,
        validate: bool = False,
    ) -> EntryUpdateResponsePydantic:
        raw_response = self.raw.create_catalog_entry(
            name=name,
            description=description,
            data_set=data_set,
            entitlements=entitlements,
            creator_entitlements=creator_entitlements,
            exchange=exchange,
        )
        if validate:
            return EntryUpdateResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EntryUpdateResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        description: typing.Optional[str] = None,
        data_set: typing.Optional[DataSetPatch] = None,
        entitlements: typing.Optional[BatchIdentityInputEntitlements] = None,
        creator_entitlements: typing.Optional[Entitlements] = None,
        exchange: typing.Optional[Exchange] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_catalog_entry_mapped_args(
            name=name,
            description=description,
            data_set=data_set,
            entitlements=entitlements,
            creator_entitlements=creator_entitlements,
            exchange=exchange,
        )
        return await self._acreate_catalog_entry_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        description: typing.Optional[str] = None,
        data_set: typing.Optional[DataSetPatch] = None,
        entitlements: typing.Optional[BatchIdentityInputEntitlements] = None,
        creator_entitlements: typing.Optional[Entitlements] = None,
        exchange: typing.Optional[Exchange] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_catalog_entry_mapped_args(
            name=name,
            description=description,
            data_set=data_set,
            entitlements=entitlements,
            creator_entitlements=creator_entitlements,
            exchange=exchange,
        )
        return self._create_catalog_entry_oapg(
            body=args.body,
        )

