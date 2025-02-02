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


class DataSetSampleData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Optional location to download sample data
    """


    class MetaOapg:
        
        class properties:
            csv = schemas.StrSchema
            json = schemas.StrSchema
            __annotations__ = {
                "csv": csv,
                "json": json,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["csv"]) -> MetaOapg.properties.csv: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["json"]) -> MetaOapg.properties.json: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["csv", "json", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["csv"]) -> typing.Union[MetaOapg.properties.csv, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["json"]) -> typing.Union[MetaOapg.properties.json, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["csv", "json", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        csv: typing.Union[MetaOapg.properties.csv, str, schemas.Unset] = schemas.unset,
        json: typing.Union[MetaOapg.properties.json, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataSetSampleData':
        return super().__new__(
            cls,
            *args,
            csv=csv,
            json=json,
            _configuration=_configuration,
            **kwargs,
        )
