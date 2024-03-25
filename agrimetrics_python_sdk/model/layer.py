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


class Layer(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "layerId",
            "description",
            "links",
        }
        
        class properties:
            description = schemas.StrSchema
            layerId = schemas.StrSchema
        
            @staticmethod
            def links() -> typing.Type['LayerLinks']:
                return LayerLinks
            __annotations__ = {
                "description": description,
                "layerId": layerId,
                "links": links,
            }
    
    layerId: MetaOapg.properties.layerId
    description: MetaOapg.properties.description
    links: 'LayerLinks'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layerId"]) -> MetaOapg.properties.layerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'LayerLinks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "layerId", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layerId"]) -> MetaOapg.properties.layerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> 'LayerLinks': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "layerId", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        layerId: typing.Union[MetaOapg.properties.layerId, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        links: 'LayerLinks',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Layer':
        return super().__new__(
            cls,
            *args,
            layerId=layerId,
            description=description,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from agrimetrics_python_sdk.model.layer_links import LayerLinks
