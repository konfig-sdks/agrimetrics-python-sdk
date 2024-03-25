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


class CategoryValue(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The value of the category
    """
    
    @schemas.classproperty
    def FREE(cls):
        return cls("free")
    
    @schemas.classproperty
    def STANDARD(cls):
        return cls("standard")
    
    @schemas.classproperty
    def PREMIUM(cls):
        return cls("premium")
    
    @schemas.classproperty
    def ONREQUEST(cls):
        return cls("on-request")
