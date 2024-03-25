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


class RequiredQueryDatasetListLayersWithinDataset404Response(TypedDict):
    message: str

class OptionalQueryDatasetListLayersWithinDataset404Response(TypedDict, total=False):
    pass

class QueryDatasetListLayersWithinDataset404Response(RequiredQueryDatasetListLayersWithinDataset404Response, OptionalQueryDatasetListLayersWithinDataset404Response):
    pass