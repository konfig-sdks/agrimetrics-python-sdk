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


class IdentityInput(BaseModel):
    # The type of the identity
    type: Literal["user", "organisation", "public"] = Field(alias='type')

    # The Auth0 id of a user, or uuid of another identity
    id: typing.Optional[str] = Field(None, alias='id')

    # The email address of a user
    email: typing.Optional[str] = Field(None, alias='email')

    # The name of the user. Will be ignored, but allowed so GET data can be round-tripped.
    name: typing.Optional[str] = Field(None, alias='name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )