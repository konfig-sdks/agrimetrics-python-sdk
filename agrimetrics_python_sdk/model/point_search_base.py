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


class PointSearchBase(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "distance",
            "geometry",
        }
        
        class properties:
        
            @staticmethod
            def geometry() -> typing.Type['GeoJSONPoint']:
                return GeoJSONPoint
            
            
            class distance(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 10
            time = schemas.DateTimeSchema
            __annotations__ = {
                "geometry": geometry,
                "distance": distance,
                "time": time,
            }
    
    distance: MetaOapg.properties.distance
    geometry: 'GeoJSONPoint'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geometry"]) -> 'GeoJSONPoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["distance"]) -> MetaOapg.properties.distance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time"]) -> MetaOapg.properties.time: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["geometry", "distance", "time", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geometry"]) -> 'GeoJSONPoint': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["distance"]) -> MetaOapg.properties.distance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time"]) -> typing.Union[MetaOapg.properties.time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["geometry", "distance", "time", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        distance: typing.Union[MetaOapg.properties.distance, decimal.Decimal, int, ],
        geometry: 'GeoJSONPoint',
        time: typing.Union[MetaOapg.properties.time, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PointSearchBase':
        return super().__new__(
            cls,
            *args,
            distance=distance,
            geometry=geometry,
            time=time,
            _configuration=_configuration,
            **kwargs,
        )

from agrimetrics_python_sdk.model.geo_json_point import GeoJSONPoint
