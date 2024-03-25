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

from agrimetrics_python_sdk.model.rest_error import RestError as RestErrorSchema

from agrimetrics_python_sdk.type.rest_error import RestError

from ...api_client import Dictionary
from agrimetrics_python_sdk.pydantic.rest_error import RestError as RestErrorPydantic

from . import path

# Query params
FormatSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'format': typing.Union[FormatSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    required=True,
    explode=True,
)
# Path params
DatasetIdSchema = schemas.UUIDSchema
LayerNameSchema = schemas.StrSchema
StyleSchema = schemas.StrSchema
ImageFormatSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'datasetId': typing.Union[DatasetIdSchema, str, uuid.UUID, ],
        'layerName': typing.Union[LayerNameSchema, str, ],
        'style': typing.Union[StyleSchema, str, ],
        'imageFormat': typing.Union[ImageFormatSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_dataset_id = api_client.PathParameter(
    name="datasetId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DatasetIdSchema,
    required=True,
)
request_path_layer_name = api_client.PathParameter(
    name="layerName",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LayerNameSchema,
    required=True,
)
request_path_style = api_client.PathParameter(
    name="style",
    style=api_client.ParameterStyle.SIMPLE,
    schema=StyleSchema,
    required=True,
)
request_path_image_format = api_client.PathParameter(
    name="imageFormat",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ImageFormatSchema,
    required=True,
)
SchemaFor200ResponseBodyTextPlain = schemas.StrSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: str


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'text/plain': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextPlain),
    },
)
SchemaFor400ResponseBodyApplicationJson = RestErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: RestError


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: RestError


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = RestErrorSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: RestError


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: RestError


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = RestErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: RestError


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: RestError


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'text/plain',
    'application/json',
)


class BaseApi(api_client.Api):

    def _query_tilejson_image_format_mapped_args(
        self,
        dataset_id: str,
        layer_name: str,
        style: str,
        image_format: str,
        format: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if format is not None:
            _query_params["format"] = format
        if dataset_id is not None:
            _path_params["datasetId"] = dataset_id
        if layer_name is not None:
            _path_params["layerName"] = layer_name
        if style is not None:
            _path_params["style"] = style
        if image_format is not None:
            _path_params["imageFormat"] = image_format
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aquery_tilejson_image_format_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        WMTS Service query
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_dataset_id,
            request_path_layer_name,
            request_path_style,
            request_path_image_format,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_format,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/datasets/{datasetId}/wmts/rest/{layerName}/{style}/tilejson/{imageFormat}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _query_tilejson_image_format_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        WMTS Service query
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_dataset_id,
            request_path_layer_name,
            request_path_style,
            request_path_image_format,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_format,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/datasets/{datasetId}/wmts/rest/{layerName}/{style}/tilejson/{imageFormat}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


class QueryTilejsonImageFormatRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aquery_tilejson_image_format(
        self,
        dataset_id: str,
        layer_name: str,
        style: str,
        image_format: str,
        format: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._query_tilejson_image_format_mapped_args(
            dataset_id=dataset_id,
            layer_name=layer_name,
            style=style,
            image_format=image_format,
            format=format,
        )
        return await self._aquery_tilejson_image_format_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def query_tilejson_image_format(
        self,
        dataset_id: str,
        layer_name: str,
        style: str,
        image_format: str,
        format: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._query_tilejson_image_format_mapped_args(
            dataset_id=dataset_id,
            layer_name=layer_name,
            style=style,
            image_format=image_format,
            format=format,
        )
        return self._query_tilejson_image_format_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class QueryTilejsonImageFormat(BaseApi):

    async def aquery_tilejson_image_format(
        self,
        dataset_id: str,
        layer_name: str,
        style: str,
        image_format: str,
        format: str,
        validate: bool = False,
        **kwargs,
    ) -> str:
        raw_response = await self.raw.aquery_tilejson_image_format(
            dataset_id=dataset_id,
            layer_name=layer_name,
            style=style,
            image_format=image_format,
            format=format,
            **kwargs,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body
    
    
    def query_tilejson_image_format(
        self,
        dataset_id: str,
        layer_name: str,
        style: str,
        image_format: str,
        format: str,
        validate: bool = False,
    ) -> str:
        raw_response = self.raw.query_tilejson_image_format(
            dataset_id=dataset_id,
            layer_name=layer_name,
            style=style,
            image_format=image_format,
            format=format,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        dataset_id: str,
        layer_name: str,
        style: str,
        image_format: str,
        format: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._query_tilejson_image_format_mapped_args(
            dataset_id=dataset_id,
            layer_name=layer_name,
            style=style,
            image_format=image_format,
            format=format,
        )
        return await self._aquery_tilejson_image_format_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        dataset_id: str,
        layer_name: str,
        style: str,
        image_format: str,
        format: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._query_tilejson_image_format_mapped_args(
            dataset_id=dataset_id,
            layer_name=layer_name,
            style=style,
            image_format=image_format,
            format=format,
        )
        return self._query_tilejson_image_format_oapg(
            query_params=args.query,
            path_params=args.path,
        )

