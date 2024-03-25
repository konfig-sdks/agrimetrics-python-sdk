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


class GeospatialExtent(BaseModel):
    north_bound_latitude: typing.Union[int, float] = Field(alias='northBoundLatitude')

    east_bound_longitude: typing.Union[int, float] = Field(alias='eastBoundLongitude')

    south_bound_latitude: typing.Union[int, float] = Field(alias='southBoundLatitude')

    west_bound_longitude: typing.Union[int, float] = Field(alias='westBoundLongitude')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )