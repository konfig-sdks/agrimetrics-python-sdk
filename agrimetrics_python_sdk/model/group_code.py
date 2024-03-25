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


class GroupCode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Name of group being harvested
    """


    class MetaOapg:
        enum_value_to_name = {
            "apha": "APHA",
            "defra": "DEFRA",
            "ea": "EA",
            "ne": "NE",
            "rpa": "RPA",
        }
    
    @schemas.classproperty
    def APHA(cls):
        return cls("apha")
    
    @schemas.classproperty
    def DEFRA(cls):
        return cls("defra")
    
    @schemas.classproperty
    def EA(cls):
        return cls("ea")
    
    @schemas.classproperty
    def NE(cls):
        return cls("ne")
    
    @schemas.classproperty
    def RPA(cls):
        return cls("rpa")