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


class RequiredConcept(TypedDict):
    # The value of the concept
    value: str

    # The label of the concept
    label: str

class OptionalConcept(TypedDict, total=False):
    pass

class Concept(RequiredConcept, OptionalConcept):
    pass