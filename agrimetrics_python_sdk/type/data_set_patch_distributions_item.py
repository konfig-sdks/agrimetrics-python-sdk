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


class RequiredDataSetPatchDistributionsItem(TypedDict):
    pass

class OptionalDataSetPatchDistributionsItem(TypedDict, total=False):
    # Description on how to access the data set.
    description: str

    # A data service that gives access to the data set.
    service: str

class DataSetPatchDistributionsItem(RequiredDataSetPatchDistributionsItem, OptionalDataSetPatchDistributionsItem):
    pass