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


class DraftStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The workflow status of this data set's draft
    """


    class MetaOapg:
        enum_value_to_name = {
            "submitted": "SUBMITTED",
            "approved": "APPROVED",
            "rejected": "REJECTED",
        }
    
    @schemas.classproperty
    def SUBMITTED(cls):
        return cls("submitted")
    
    @schemas.classproperty
    def APPROVED(cls):
        return cls("approved")
    
    @schemas.classproperty
    def REJECTED(cls):
        return cls("rejected")