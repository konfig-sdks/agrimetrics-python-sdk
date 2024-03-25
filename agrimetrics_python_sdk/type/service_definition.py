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

from agrimetrics_python_sdk.type.billable import Billable

class RequiredServiceDefinition(TypedDict):
    datasetId: str

    layerName: str

    service: str

    WFS: str

    WCS: str

    WMS: str

    WMTS: str

    OGCApiFeatures: str

    OGCApiTiles: str

class OptionalServiceDefinition(TypedDict, total=False):
    temporal: bool

    datastore: str

    geoserverHostName: str

    geometryField: str

    billable: Billable

    defaultEPSGCode: typing.Union[int, float]

class ServiceDefinition(RequiredServiceDefinition, OptionalServiceDefinition):
    pass
