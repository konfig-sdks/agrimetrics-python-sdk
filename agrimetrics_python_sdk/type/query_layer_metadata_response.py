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

from agrimetrics_python_sdk.type.bounding_box import BoundingBox
from agrimetrics_python_sdk.type.output_formats import OutputFormats
from agrimetrics_python_sdk.type.query_layer_metadata_response_links import QueryLayerMetadataResponseLinks
from agrimetrics_python_sdk.type.times import Times

class RequiredQueryLayerMetadataResponse(TypedDict):
    description: str

    layerId: str

    links: QueryLayerMetadataResponseLinks

    geometry: BoundingBox

    outputFormats: typing.List[OutputFormats]

class OptionalQueryLayerMetadataResponse(TypedDict, total=False):
    times: Times

class QueryLayerMetadataResponse(RequiredQueryLayerMetadataResponse, OptionalQueryLayerMetadataResponse):
    pass