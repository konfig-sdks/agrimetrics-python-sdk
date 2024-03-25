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


class NewLayers(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class layers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ServiceDefinitionResponse']:
                        return ServiceDefinitionResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ServiceDefinitionResponse'], typing.List['ServiceDefinitionResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'layers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ServiceDefinitionResponse':
                    return super().__getitem__(i)
            layerId = schemas.StrSchema
            __annotations__ = {
                "layers": layers,
                "layerId": layerId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layers"]) -> MetaOapg.properties.layers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layerId"]) -> MetaOapg.properties.layerId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["layers", "layerId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layers"]) -> typing.Union[MetaOapg.properties.layers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layerId"]) -> typing.Union[MetaOapg.properties.layerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["layers", "layerId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        layers: typing.Union[MetaOapg.properties.layers, list, tuple, schemas.Unset] = schemas.unset,
        layerId: typing.Union[MetaOapg.properties.layerId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewLayers':
        return super().__new__(
            cls,
            *args,
            layers=layers,
            layerId=layerId,
            _configuration=_configuration,
            **kwargs,
        )

from agrimetrics_python_sdk.model.service_definition_response import ServiceDefinitionResponse