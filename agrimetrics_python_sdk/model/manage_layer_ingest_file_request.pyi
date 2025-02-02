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


class ManageLayerIngestFileRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "fileId",
        }
        
        class properties:
            fileId = schemas.StrSchema
            
            
            class fileName(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def datetime() -> typing.Type['ISO8601Datetime']:
                return ISO8601Datetime
            __annotations__ = {
                "fileId": fileId,
                "fileName": fileName,
                "datetime": datetime,
            }
    
    fileId: MetaOapg.properties.fileId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileId"]) -> MetaOapg.properties.fileId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datetime"]) -> 'ISO8601Datetime': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fileId", "fileName", "datetime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileId"]) -> MetaOapg.properties.fileId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> typing.Union[MetaOapg.properties.fileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datetime"]) -> typing.Union['ISO8601Datetime', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fileId", "fileName", "datetime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        fileId: typing.Union[MetaOapg.properties.fileId, str, ],
        fileName: typing.Union[MetaOapg.properties.fileName, str, schemas.Unset] = schemas.unset,
        datetime: typing.Union['ISO8601Datetime', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManageLayerIngestFileRequest':
        return super().__new__(
            cls,
            *args,
            fileId=fileId,
            fileName=fileName,
            datetime=datetime,
            _configuration=_configuration,
            **kwargs,
        )

from agrimetrics_python_sdk.model.iso8601_datetime import ISO8601Datetime
