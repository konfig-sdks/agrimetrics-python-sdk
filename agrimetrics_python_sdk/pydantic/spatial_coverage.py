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


SpatialCoverage = Literal["United Kingdom", "England", "Northern Ireland", "Scotland", "Wales", "Canada", "Ethiopia", "France", "India", "Kenya", "Mexico", "Netherlands", "Spain", "Tanzania", "Uganda", "United States", "Global only"]
