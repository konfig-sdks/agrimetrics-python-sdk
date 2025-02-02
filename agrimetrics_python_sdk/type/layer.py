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

from agrimetrics_python_sdk.type.layer_links import LayerLinks

class RequiredLayer(TypedDict):
    description: str

    layerId: str

    links: LayerLinks

class OptionalLayer(TypedDict, total=False):
    pass

class Layer(RequiredLayer, OptionalLayer):
    pass
