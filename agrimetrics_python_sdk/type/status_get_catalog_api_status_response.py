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

from agrimetrics_python_sdk.type.status_get_catalog_api_status_response_links import StatusGetCatalogApiStatusResponseLinks

class RequiredStatusGetCatalogApiStatusResponse(TypedDict):
    version: str

    _links: StatusGetCatalogApiStatusResponseLinks

class OptionalStatusGetCatalogApiStatusResponse(TypedDict, total=False):
    pass

class StatusGetCatalogApiStatusResponse(RequiredStatusGetCatalogApiStatusResponse, OptionalStatusGetCatalogApiStatusResponse):
    pass