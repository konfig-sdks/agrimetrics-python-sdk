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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from agrimetrics_python_sdk.pydantic.epsg4326_latitude import EPSG4326Latitude
from agrimetrics_python_sdk.pydantic.epsg4326_longitude import EPSG4326Longitude

class BoundingBoxCoordinates(BaseModel):
    minlat: EPSG4326Latitude = Field(alias='minlat')

    minlon: EPSG4326Longitude = Field(alias='minlon')

    maxlat: EPSG4326Latitude = Field(alias='maxlat')

    maxlon: EPSG4326Longitude = Field(alias='maxlon')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
