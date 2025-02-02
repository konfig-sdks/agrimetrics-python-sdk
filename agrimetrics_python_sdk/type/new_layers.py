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

from agrimetrics_python_sdk.type.service_definition_response import ServiceDefinitionResponse

class RequiredNewLayers(TypedDict):
    pass

class OptionalNewLayers(TypedDict, total=False):
    layers: typing.List[ServiceDefinitionResponse]

    layerId: str

class NewLayers(RequiredNewLayers, OptionalNewLayers):
    pass
