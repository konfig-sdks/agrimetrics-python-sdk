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


class RequiredDataRequest(TypedDict):
    # The name of the project the data is for
    projectName: str

    # The name of the project manager who can approve the request
    projectManagerName: str

    # The email address of the project manager who can approve the request
    projectManagerEmail: str

    # The ID of the dataset that the data request relates to
    datasetId: str

    # The name of the dataset that the data request relates to
    datasetName: str

    # The format the user would like the data to be provided in
    requestedFormat: str

class OptionalDataRequest(TypedDict, total=False):
    # The area of interest that the user is requesting access to as a stringified GeoJSON
    geoJsonAOI: str

    # The area of interest that the user is requesting access to as a zipped shapefile
    shapefileAOI: typing.IO

class DataRequest(RequiredDataRequest, OptionalDataRequest):
    pass