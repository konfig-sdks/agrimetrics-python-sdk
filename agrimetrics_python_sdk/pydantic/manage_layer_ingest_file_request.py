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

from agrimetrics_python_sdk.pydantic.iso8601_datetime import ISO8601Datetime

class ManageLayerIngestFileRequest(BaseModel):
    file_id: str = Field(alias='fileId')

    file_name: typing.Optional[str] = Field(None, alias='fileName')

    datetime: typing.Optional[ISO8601Datetime] = Field(None, alias='datetime')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
