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


class Contact(BaseModel):
    # Organisation name for this contact
    organisation_name: str = Field(alias='organisationName')

    # The role of this contact as it relates to the data set
    role: Literal["resourceProvider", "custodian", "owner", "user", "distributor", "originator", "pointOfContact", "principalInvestigator", "processor", "publisher", "author"] = Field(alias='role')

    # Individual name for this contact
    individual_name: typing.Optional[str] = Field(None, alias='individualName')

    # Position of this contact within their organisation
    position_name: typing.Optional[str] = Field(None, alias='positionName')

    # Email address for this contact
    email_address: typing.Optional[str] = Field(None, alias='emailAddress')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )