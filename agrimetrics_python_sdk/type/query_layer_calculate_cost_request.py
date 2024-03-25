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

from agrimetrics_python_sdk.type.point_search_base import PointSearchBase
from agrimetrics_python_sdk.type.polygon_or_b_box_search_base import PolygonOrBBoxSearchBase

QueryLayerCalculateCostRequest = typing.Union[PolygonOrBBoxSearchBase,PointSearchBase]