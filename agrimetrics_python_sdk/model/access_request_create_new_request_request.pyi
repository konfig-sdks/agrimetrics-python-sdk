# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
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

from agrimetrics_python_sdk import schemas  # noqa: F401


class AccessRequestCreateNewRequestRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "requestMessage",
            "dataSetId",
            "requestingEntityId",
        }
        
        class properties:
            dataSetId = schemas.UUIDSchema
            requestingEntityId = schemas.StrSchema
            requestMessage = schemas.StrSchema
            requesterName = schemas.StrSchema
            requesterEmail = schemas.StrSchema
            __annotations__ = {
                "dataSetId": dataSetId,
                "requestingEntityId": requestingEntityId,
                "requestMessage": requestMessage,
                "requesterName": requesterName,
                "requesterEmail": requesterEmail,
            }
    
    requestMessage: MetaOapg.properties.requestMessage
    dataSetId: MetaOapg.properties.dataSetId
    requestingEntityId: MetaOapg.properties.requestingEntityId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataSetId"]) -> MetaOapg.properties.dataSetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestingEntityId"]) -> MetaOapg.properties.requestingEntityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestMessage"]) -> MetaOapg.properties.requestMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requesterName"]) -> MetaOapg.properties.requesterName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requesterEmail"]) -> MetaOapg.properties.requesterEmail: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dataSetId", "requestingEntityId", "requestMessage", "requesterName", "requesterEmail", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataSetId"]) -> MetaOapg.properties.dataSetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestingEntityId"]) -> MetaOapg.properties.requestingEntityId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestMessage"]) -> MetaOapg.properties.requestMessage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requesterName"]) -> typing.Union[MetaOapg.properties.requesterName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requesterEmail"]) -> typing.Union[MetaOapg.properties.requesterEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dataSetId", "requestingEntityId", "requestMessage", "requesterName", "requesterEmail", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        requestMessage: typing.Union[MetaOapg.properties.requestMessage, str, ],
        dataSetId: typing.Union[MetaOapg.properties.dataSetId, str, uuid.UUID, ],
        requestingEntityId: typing.Union[MetaOapg.properties.requestingEntityId, str, ],
        requesterName: typing.Union[MetaOapg.properties.requesterName, str, schemas.Unset] = schemas.unset,
        requesterEmail: typing.Union[MetaOapg.properties.requesterEmail, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessRequestCreateNewRequestRequest':
        return super().__new__(
            cls,
            *args,
            requestMessage=requestMessage,
            dataSetId=dataSetId,
            requestingEntityId=requestingEntityId,
            requesterName=requesterName,
            requesterEmail=requesterEmail,
            _configuration=_configuration,
            **kwargs,
        )