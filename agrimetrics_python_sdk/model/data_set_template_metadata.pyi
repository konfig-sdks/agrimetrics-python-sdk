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


class DataSetTemplateMetadata(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Used as params for POST/PUT requests
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            description = schemas.StrSchema
        
            @staticmethod
            def dataSet() -> typing.Type['DataSetPatch']:
                return DataSetPatch
        
            @staticmethod
            def entitlements() -> typing.Type['BatchIdentityInputEntitlements']:
                return BatchIdentityInputEntitlements
        
            @staticmethod
            def creatorEntitlements() -> typing.Type['Entitlements']:
                return Entitlements
        
            @staticmethod
            def exchange() -> typing.Type['Exchange']:
                return Exchange
            __annotations__ = {
                "name": name,
                "description": description,
                "dataSet": dataSet,
                "entitlements": entitlements,
                "creatorEntitlements": creatorEntitlements,
                "exchange": exchange,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataSet"]) -> 'DataSetPatch': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entitlements"]) -> 'BatchIdentityInputEntitlements': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creatorEntitlements"]) -> 'Entitlements': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exchange"]) -> 'Exchange': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "dataSet", "entitlements", "creatorEntitlements", "exchange", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataSet"]) -> typing.Union['DataSetPatch', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entitlements"]) -> typing.Union['BatchIdentityInputEntitlements', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creatorEntitlements"]) -> typing.Union['Entitlements', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exchange"]) -> typing.Union['Exchange', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "dataSet", "entitlements", "creatorEntitlements", "exchange", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        dataSet: typing.Union['DataSetPatch', schemas.Unset] = schemas.unset,
        entitlements: typing.Union['BatchIdentityInputEntitlements', schemas.Unset] = schemas.unset,
        creatorEntitlements: typing.Union['Entitlements', schemas.Unset] = schemas.unset,
        exchange: typing.Union['Exchange', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataSetTemplateMetadata':
        return super().__new__(
            cls,
            *args,
            name=name,
            description=description,
            dataSet=dataSet,
            entitlements=entitlements,
            creatorEntitlements=creatorEntitlements,
            exchange=exchange,
            _configuration=_configuration,
            **kwargs,
        )

from agrimetrics_python_sdk.model.batch_identity_input_entitlements import BatchIdentityInputEntitlements
from agrimetrics_python_sdk.model.data_set_patch import DataSetPatch
from agrimetrics_python_sdk.model.entitlements import Entitlements
from agrimetrics_python_sdk.model.exchange import Exchange
