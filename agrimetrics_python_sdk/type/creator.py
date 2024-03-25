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


class RequiredCreator(TypedDict):
    pass

class OptionalCreator(TypedDict, total=False):
    # The value of the creator
    value: str

    # The label of the creator
    label: str

class Creator(RequiredCreator, OptionalCreator):
    pass