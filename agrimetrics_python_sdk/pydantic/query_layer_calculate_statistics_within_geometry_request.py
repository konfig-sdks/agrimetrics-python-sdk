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

from agrimetrics_python_sdk.pydantic.general_geometry import GeneralGeometry

class QueryLayerCalculateStatisticsWithinGeometryRequest(BaseModel):
    geometry: GeneralGeometry = Field(alias='geometry')

    time: typing.Optional[datetime] = Field(None, alias='time')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
