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


class RequiredResource(TypedDict):
    # URL to obtain more information on this data set.
    url: str

class OptionalResource(TypedDict, total=False):
    # Description of what the URL represents.
    description: str

    # ID for this resource item.
    id: str

    # Name for what the URL represents.
    name: str

    # Indicates whether the resource metadata is sensitive data.
    private: bool

class Resource(RequiredResource, OptionalResource):
    pass
