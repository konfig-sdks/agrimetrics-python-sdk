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

from agrimetrics_python_sdk.pydantic.image_representation_author import ImageRepresentationAuthor

class ImageRepresentation(BaseModel):
    type: typing.Optional[str] = Field(None, alias='type')

    url: typing.Optional[str] = Field(None, alias='url')

    thumbnail_url: typing.Optional[str] = Field(None, alias='thumbnailUrl')

    author: typing.Optional[ImageRepresentationAuthor] = Field(None, alias='author')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
