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


class RequiredDataSetPatchGeospatialExtent(TypedDict):
    northBoundLatitude: typing.Union[int, float]

    eastBoundLongitude: typing.Union[int, float]

    southBoundLatitude: typing.Union[int, float]

    westBoundLongitude: typing.Union[int, float]

class OptionalDataSetPatchGeospatialExtent(TypedDict, total=False):
    pass

class DataSetPatchGeospatialExtent(RequiredDataSetPatchGeospatialExtent, OptionalDataSetPatchGeospatialExtent):
    pass