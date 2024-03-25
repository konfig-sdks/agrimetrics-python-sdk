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


class AuthenticationGetJwtResponseJwts(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def agrimetrics() -> typing.Type['AuthenticationGetJwtResponseJwtsAgrimetrics']:
                return AuthenticationGetJwtResponseJwtsAgrimetrics
            __annotations__ = {
                "agrimetrics": agrimetrics,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agrimetrics"]) -> 'AuthenticationGetJwtResponseJwtsAgrimetrics': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["agrimetrics", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agrimetrics"]) -> typing.Union['AuthenticationGetJwtResponseJwtsAgrimetrics', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["agrimetrics", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        agrimetrics: typing.Union['AuthenticationGetJwtResponseJwtsAgrimetrics', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthenticationGetJwtResponseJwts':
        return super().__new__(
            cls,
            *args,
            agrimetrics=agrimetrics,
            _configuration=_configuration,
            **kwargs,
        )

from agrimetrics_python_sdk.model.authentication_get_jwt_response_jwts_agrimetrics import AuthenticationGetJwtResponseJwtsAgrimetrics
