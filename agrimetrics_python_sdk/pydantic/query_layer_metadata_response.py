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

from agrimetrics_python_sdk.pydantic.bounding_box import BoundingBox
from agrimetrics_python_sdk.pydantic.output_formats import OutputFormats
from agrimetrics_python_sdk.pydantic.query_layer_metadata_response_links import QueryLayerMetadataResponseLinks
from agrimetrics_python_sdk.pydantic.times import Times

class QueryLayerMetadataResponse(BaseModel):
    description: str = Field(alias='description')

    layer_id: str = Field(alias='layerId')

    links: QueryLayerMetadataResponseLinks = Field(alias='links')

    geometry: BoundingBox = Field(alias='geometry')

    output_formats: typing.List[OutputFormats] = Field(alias='outputFormats')

    times: typing.Optional[Times] = Field(None, alias='times')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )