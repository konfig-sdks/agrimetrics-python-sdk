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


class WorkflowKeywords(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Workflow keyword value
    """
    
    @schemas.classproperty
    def OPEN_DATA(cls):
        return cls("OpenData")
    
    @schemas.classproperty
    def NON_SPATIAL(cls):
        return cls("NonSpatial")
    
    @schemas.classproperty
    def NOT_OPEN(cls):
        return cls("NotOpen")
    
    @schemas.classproperty
    def CONDITIONAL_DATA(cls):
        return cls("ConditionalData")
    
    @schemas.classproperty
    def PARTNER_DATASET(cls):
        return cls("PartnerDataset")
    
    @schemas.classproperty
    def INTERNAL_ONLY(cls):
        return cls("InternalOnly")
    
    @schemas.classproperty
    def THIRD_PARTY(cls):
        return cls("ThirdParty")
    
    @schemas.classproperty
    def DATASET_BUNDLE(cls):
        return cls("DatasetBundle")
    
    @schemas.classproperty
    def RETIRED_OPEN_DATA(cls):
        return cls("RetiredOpenData")
    
    @schemas.classproperty
    def RETIRED_NOT_OPEN(cls):
        return cls("RetiredNotOpen")
    
    @schemas.classproperty
    def RETIRED_CONDITIONAL_DATA(cls):
        return cls("RetiredConditionalData")
    
    @schemas.classproperty
    def RETIRED_PARTNER_DATASET(cls):
        return cls("RetiredPartnerDataset")
    
    @schemas.classproperty
    def RETIRED_INTERNAL_ONLY(cls):
        return cls("RetiredInternalOnly")
    
    @schemas.classproperty
    def RETIRED_THIRD_PARTY(cls):
        return cls("RetiredThirdParty")
    
    @schemas.classproperty
    def RETIRED_DATASET_BUNDLE(cls):
        return cls("RetiredDatasetBundle")
    
    @schemas.classproperty
    def RETIRED_NON_SPATIAL(cls):
        return cls("RetiredNonSpatial")
