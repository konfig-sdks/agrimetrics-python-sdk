# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from agrimetrics_python_sdk.type.exchange import Exchange

class RequiredCreateFromTemplatePayload(TypedDict):
    # The ID of a template in the catalog
    templateId: str

class OptionalCreateFromTemplatePayload(TypedDict, total=False):
    # Title for the data set.
    title: str

    # Description of the data set.
    description: str

    exchange: Exchange

class CreateFromTemplatePayload(RequiredCreateFromTemplatePayload, OptionalCreateFromTemplatePayload):
    pass
