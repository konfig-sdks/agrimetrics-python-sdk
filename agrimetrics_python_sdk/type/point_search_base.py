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

from agrimetrics_python_sdk.type.geo_json_point import GeoJSONPoint

class RequiredPointSearchBase(TypedDict):
    geometry: GeoJSONPoint

    distance: int

class OptionalPointSearchBase(TypedDict, total=False):
    time: datetime

class PointSearchBase(RequiredPointSearchBase, OptionalPointSearchBase):
    pass
