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


class BatchIdentityInputEntitlements(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['BatchIdentityInputEntitlementsItem']:
            return BatchIdentityInputEntitlementsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['BatchIdentityInputEntitlementsItem'], typing.List['BatchIdentityInputEntitlementsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BatchIdentityInputEntitlements':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'BatchIdentityInputEntitlementsItem':
        return super().__getitem__(i)

from agrimetrics_python_sdk.model.batch_identity_input_entitlements_item import BatchIdentityInputEntitlementsItem
