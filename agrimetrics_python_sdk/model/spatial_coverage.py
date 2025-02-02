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


class SpatialCoverage(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The geo spatial coverage of the data set.
    """


    class MetaOapg:
        enum_value_to_name = {
            "United Kingdom": "UNITED_KINGDOM",
            "England": "ENGLAND",
            "Northern Ireland": "NORTHERN_IRELAND",
            "Scotland": "SCOTLAND",
            "Wales": "WALES",
            "Canada": "CANADA",
            "Ethiopia": "ETHIOPIA",
            "France": "FRANCE",
            "India": "INDIA",
            "Kenya": "KENYA",
            "Mexico": "MEXICO",
            "Netherlands": "NETHERLANDS",
            "Spain": "SPAIN",
            "Tanzania": "TANZANIA",
            "Uganda": "UGANDA",
            "United States": "UNITED_STATES",
            "Global only": "GLOBAL_ONLY",
        }
    
    @schemas.classproperty
    def UNITED_KINGDOM(cls):
        return cls("United Kingdom")
    
    @schemas.classproperty
    def ENGLAND(cls):
        return cls("England")
    
    @schemas.classproperty
    def NORTHERN_IRELAND(cls):
        return cls("Northern Ireland")
    
    @schemas.classproperty
    def SCOTLAND(cls):
        return cls("Scotland")
    
    @schemas.classproperty
    def WALES(cls):
        return cls("Wales")
    
    @schemas.classproperty
    def CANADA(cls):
        return cls("Canada")
    
    @schemas.classproperty
    def ETHIOPIA(cls):
        return cls("Ethiopia")
    
    @schemas.classproperty
    def FRANCE(cls):
        return cls("France")
    
    @schemas.classproperty
    def INDIA(cls):
        return cls("India")
    
    @schemas.classproperty
    def KENYA(cls):
        return cls("Kenya")
    
    @schemas.classproperty
    def MEXICO(cls):
        return cls("Mexico")
    
    @schemas.classproperty
    def NETHERLANDS(cls):
        return cls("Netherlands")
    
    @schemas.classproperty
    def SPAIN(cls):
        return cls("Spain")
    
    @schemas.classproperty
    def TANZANIA(cls):
        return cls("Tanzania")
    
    @schemas.classproperty
    def UGANDA(cls):
        return cls("Uganda")
    
    @schemas.classproperty
    def UNITED_STATES(cls):
        return cls("United States")
    
    @schemas.classproperty
    def GLOBAL_ONLY(cls):
        return cls("Global only")
