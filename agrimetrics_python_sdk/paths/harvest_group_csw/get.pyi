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

from agrimetrics_python_sdk.model.group_code import GroupCode as GroupCodeSchema

from agrimetrics_python_sdk.type.group_code import GroupCode

from ...api_client import Dictionary
from agrimetrics_python_sdk.pydantic.group_code import GroupCode as GroupCodePydantic

# Query params


class ServiceSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CSW(cls):
        return cls("CSW")


class RequestSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def GET_RECORDS(cls):
        return cls("GetRecords")
    
    @schemas.classproperty
    def GET_RECORD_BY_ID(cls):
        return cls("GetRecordById")
    
    @schemas.classproperty
    def GET_CAPABILITIES(cls):
        return cls("GetCapabilities")
VersionSchema = schemas.StrSchema


class StartPositionSchema(
    schemas.NumberSchema
):
    pass


class MaxRecordsSchema(
    schemas.NumberSchema
):
    pass


class IdSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.UUIDSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, uuid.UUID, ]], typing.List[typing.Union[MetaOapg.items, str, uuid.UUID, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IdSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class OutputSchemaSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def HTTP__WWW_ISOTC211_ORG_2005_GMD(cls):
        return cls("http://www.isotc211.org/2005/gmd")


class ElementsetnameSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def FULL(cls):
        return cls("full")
    
    @schemas.classproperty
    def BRIEF(cls):
        return cls("brief")
    
    @schemas.classproperty
    def SUMMARY(cls):
        return cls("summary")


class OutputFormatSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def APPLICATION_XML(cls):
        return cls("application/xml")


class TypeNamesSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def GMDMD_METADATA(cls):
        return cls("gmd:MD_Metadata")
    
    @schemas.classproperty
    def CSWRECORD(cls):
        return cls("csw:Record")
ResultTypeSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'service': typing.Union[ServiceSchema, str, ],
        'request': typing.Union[RequestSchema, str, ],
        'version': typing.Union[VersionSchema, str, ],
        'startPosition': typing.Union[StartPositionSchema, decimal.Decimal, int, float, ],
        'maxRecords': typing.Union[MaxRecordsSchema, decimal.Decimal, int, float, ],
        'id': typing.Union[IdSchema, list, tuple, ],
        'outputSchema': typing.Union[OutputSchemaSchema, str, ],
        'elementsetname': typing.Union[ElementsetnameSchema, str, ],
        'outputFormat': typing.Union[OutputFormatSchema, str, ],
        'typeNames': typing.Union[TypeNamesSchema, str, ],
        'resultType': typing.Union[ResultTypeSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_service = api_client.QueryParameter(
    name="service",
    style=api_client.ParameterStyle.FORM,
    schema=ServiceSchema,
    explode=True,
)
request_query_request = api_client.QueryParameter(
    name="request",
    style=api_client.ParameterStyle.FORM,
    schema=RequestSchema,
    explode=True,
)
request_query_version = api_client.QueryParameter(
    name="version",
    style=api_client.ParameterStyle.FORM,
    schema=VersionSchema,
    explode=True,
)
request_query_start_position = api_client.QueryParameter(
    name="startPosition",
    style=api_client.ParameterStyle.FORM,
    schema=StartPositionSchema,
    explode=True,
)
request_query_max_records = api_client.QueryParameter(
    name="maxRecords",
    style=api_client.ParameterStyle.FORM,
    schema=MaxRecordsSchema,
    explode=True,
)
request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
    explode=True,
)
request_query_output_schema = api_client.QueryParameter(
    name="outputSchema",
    style=api_client.ParameterStyle.FORM,
    schema=OutputSchemaSchema,
    explode=True,
)
request_query_elementsetname = api_client.QueryParameter(
    name="elementsetname",
    style=api_client.ParameterStyle.FORM,
    schema=ElementsetnameSchema,
    explode=True,
)
request_query_output_format = api_client.QueryParameter(
    name="outputFormat",
    style=api_client.ParameterStyle.FORM,
    schema=OutputFormatSchema,
    explode=True,
)
request_query_type_names = api_client.QueryParameter(
    name="typeNames",
    style=api_client.ParameterStyle.FORM,
    schema=TypeNamesSchema,
    explode=True,
)
request_query_result_type = api_client.QueryParameter(
    name="resultType",
    style=api_client.ParameterStyle.FORM,
    schema=ResultTypeSchema,
    explode=True,
)
# Path params
GroupSchema = GroupCodeSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'group': typing.Union[GroupCodeSchema, ],
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


request_path_group = api_client.PathParameter(
    name="group",
    style=api_client.ParameterStyle.SIMPLE,
    schema=GroupCodeSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationXml = schemas.DictSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXml),
    },
)
_all_accept_content_types = (
    'application/xml',
)


class BaseApi(api_client.Api):

    def _xml_data_on_group_mapped_args(
        self,
        group: GroupCode,
        service: typing.Optional[str] = None,
        request: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        start_position: typing.Optional[typing.Union[int, float]] = None,
        max_records: typing.Optional[typing.Union[int, float]] = None,
        id: typing.Optional[typing.List[str]] = None,
        output_schema: typing.Optional[str] = None,
        elementsetname: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        type_names: typing.Optional[str] = None,
        result_type: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if service is not None:
            _query_params["service"] = service
        if request is not None:
            _query_params["request"] = request
        if version is not None:
            _query_params["version"] = version
        if start_position is not None:
            _query_params["startPosition"] = start_position
        if max_records is not None:
            _query_params["maxRecords"] = max_records
        if id is not None:
            _query_params["id"] = id
        if output_schema is not None:
            _query_params["outputSchema"] = output_schema
        if elementsetname is not None:
            _query_params["elementsetname"] = elementsetname
        if output_format is not None:
            _query_params["outputFormat"] = output_format
        if type_names is not None:
            _query_params["typeNames"] = type_names
        if result_type is not None:
            _query_params["resultType"] = result_type
        if group is not None:
            _path_params["group"] = group
        args.query = _query_params
        args.path = _path_params
        return args

    async def _axml_data_on_group_oapg(
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
        Harvest xml data on the given group
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_group,
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
            request_query_service,
            request_query_request,
            request_query_version,
            request_query_start_position,
            request_query_max_records,
            request_query_id,
            request_query_output_schema,
            request_query_elementsetname,
            request_query_output_format,
            request_query_type_names,
            request_query_result_type,
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
            path_template='/harvest/{group}/csw',
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


    def _xml_data_on_group_oapg(
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
        Harvest xml data on the given group
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_group,
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
            request_query_service,
            request_query_request,
            request_query_version,
            request_query_start_position,
            request_query_max_records,
            request_query_id,
            request_query_output_schema,
            request_query_elementsetname,
            request_query_output_format,
            request_query_type_names,
            request_query_result_type,
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
            path_template='/harvest/{group}/csw',
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


class XmlDataOnGroupRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def axml_data_on_group(
        self,
        group: GroupCode,
        service: typing.Optional[str] = None,
        request: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        start_position: typing.Optional[typing.Union[int, float]] = None,
        max_records: typing.Optional[typing.Union[int, float]] = None,
        id: typing.Optional[typing.List[str]] = None,
        output_schema: typing.Optional[str] = None,
        elementsetname: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        type_names: typing.Optional[str] = None,
        result_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._xml_data_on_group_mapped_args(
            group=group,
            service=service,
            request=request,
            version=version,
            start_position=start_position,
            max_records=max_records,
            id=id,
            output_schema=output_schema,
            elementsetname=elementsetname,
            output_format=output_format,
            type_names=type_names,
            result_type=result_type,
        )
        return await self._axml_data_on_group_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def xml_data_on_group(
        self,
        group: GroupCode,
        service: typing.Optional[str] = None,
        request: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        start_position: typing.Optional[typing.Union[int, float]] = None,
        max_records: typing.Optional[typing.Union[int, float]] = None,
        id: typing.Optional[typing.List[str]] = None,
        output_schema: typing.Optional[str] = None,
        elementsetname: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        type_names: typing.Optional[str] = None,
        result_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._xml_data_on_group_mapped_args(
            group=group,
            service=service,
            request=request,
            version=version,
            start_position=start_position,
            max_records=max_records,
            id=id,
            output_schema=output_schema,
            elementsetname=elementsetname,
            output_format=output_format,
            type_names=type_names,
            result_type=result_type,
        )
        return self._xml_data_on_group_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class XmlDataOnGroup(BaseApi):

    async def axml_data_on_group(
        self,
        group: GroupCode,
        service: typing.Optional[str] = None,
        request: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        start_position: typing.Optional[typing.Union[int, float]] = None,
        max_records: typing.Optional[typing.Union[int, float]] = None,
        id: typing.Optional[typing.List[str]] = None,
        output_schema: typing.Optional[str] = None,
        elementsetname: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        type_names: typing.Optional[str] = None,
        result_type: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.axml_data_on_group(
            group=group,
            service=service,
            request=request,
            version=version,
            start_position=start_position,
            max_records=max_records,
            id=id,
            output_schema=output_schema,
            elementsetname=elementsetname,
            output_format=output_format,
            type_names=type_names,
            result_type=result_type,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def xml_data_on_group(
        self,
        group: GroupCode,
        service: typing.Optional[str] = None,
        request: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        start_position: typing.Optional[typing.Union[int, float]] = None,
        max_records: typing.Optional[typing.Union[int, float]] = None,
        id: typing.Optional[typing.List[str]] = None,
        output_schema: typing.Optional[str] = None,
        elementsetname: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        type_names: typing.Optional[str] = None,
        result_type: typing.Optional[str] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.xml_data_on_group(
            group=group,
            service=service,
            request=request,
            version=version,
            start_position=start_position,
            max_records=max_records,
            id=id,
            output_schema=output_schema,
            elementsetname=elementsetname,
            output_format=output_format,
            type_names=type_names,
            result_type=result_type,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        group: GroupCode,
        service: typing.Optional[str] = None,
        request: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        start_position: typing.Optional[typing.Union[int, float]] = None,
        max_records: typing.Optional[typing.Union[int, float]] = None,
        id: typing.Optional[typing.List[str]] = None,
        output_schema: typing.Optional[str] = None,
        elementsetname: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        type_names: typing.Optional[str] = None,
        result_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._xml_data_on_group_mapped_args(
            group=group,
            service=service,
            request=request,
            version=version,
            start_position=start_position,
            max_records=max_records,
            id=id,
            output_schema=output_schema,
            elementsetname=elementsetname,
            output_format=output_format,
            type_names=type_names,
            result_type=result_type,
        )
        return await self._axml_data_on_group_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        group: GroupCode,
        service: typing.Optional[str] = None,
        request: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        start_position: typing.Optional[typing.Union[int, float]] = None,
        max_records: typing.Optional[typing.Union[int, float]] = None,
        id: typing.Optional[typing.List[str]] = None,
        output_schema: typing.Optional[str] = None,
        elementsetname: typing.Optional[str] = None,
        output_format: typing.Optional[str] = None,
        type_names: typing.Optional[str] = None,
        result_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._xml_data_on_group_mapped_args(
            group=group,
            service=service,
            request=request,
            version=version,
            start_position=start_position,
            max_records=max_records,
            id=id,
            output_schema=output_schema,
            elementsetname=elementsetname,
            output_format=output_format,
            type_names=type_names,
            result_type=result_type,
        )
        return self._xml_data_on_group_oapg(
            query_params=args.query,
            path_params=args.path,
        )

