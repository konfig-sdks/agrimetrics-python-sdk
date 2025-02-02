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


class RequiredStatusGetCatalogApiStatusResponseLinksSelf(TypedDict):
    href: str

class OptionalStatusGetCatalogApiStatusResponseLinksSelf(TypedDict, total=False):
    pass

class StatusGetCatalogApiStatusResponseLinksSelf(RequiredStatusGetCatalogApiStatusResponseLinksSelf, OptionalStatusGetCatalogApiStatusResponseLinksSelf):
    pass
