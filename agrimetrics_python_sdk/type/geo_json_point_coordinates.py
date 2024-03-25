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

from agrimetrics_python_sdk.type.epsg4326_latitude import EPSG4326Latitude
from agrimetrics_python_sdk.type.epsg4326_longitude import EPSG4326Longitude

GeoJSONPointCoordinates = typing.List[typing.Union[typing.List[EPSG4326Longitude], typing.List[EPSG4326Latitude]]]