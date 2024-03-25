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


class BandStats(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "std",
            "min",
            "median",
            "max",
            "mean",
        }
        
        class properties:
            min = schemas.NumberSchema
            mean = schemas.NumberSchema
            median = schemas.NumberSchema
            max = schemas.NumberSchema
            std = schemas.NumberSchema
            __annotations__ = {
                "min": min,
                "mean": mean,
                "median": median,
                "max": max,
                "std": std,
            }
    
    std: MetaOapg.properties.std
    min: MetaOapg.properties.min
    median: MetaOapg.properties.median
    max: MetaOapg.properties.max
    mean: MetaOapg.properties.mean
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mean"]) -> MetaOapg.properties.mean: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["median"]) -> MetaOapg.properties.median: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["std"]) -> MetaOapg.properties.std: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["min", "mean", "median", "max", "std", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mean"]) -> MetaOapg.properties.mean: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["median"]) -> MetaOapg.properties.median: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["std"]) -> MetaOapg.properties.std: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["min", "mean", "median", "max", "std", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        std: typing.Union[MetaOapg.properties.std, decimal.Decimal, int, float, ],
        min: typing.Union[MetaOapg.properties.min, decimal.Decimal, int, float, ],
        median: typing.Union[MetaOapg.properties.median, decimal.Decimal, int, float, ],
        max: typing.Union[MetaOapg.properties.max, decimal.Decimal, int, float, ],
        mean: typing.Union[MetaOapg.properties.mean, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BandStats':
        return super().__new__(
            cls,
            *args,
            std=std,
            min=min,
            median=median,
            max=max,
            mean=mean,
            _configuration=_configuration,
            **kwargs,
        )