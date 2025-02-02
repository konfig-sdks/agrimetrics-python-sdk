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


class RequiredIdentityInput(TypedDict):
    # The type of the identity
    type: str

class OptionalIdentityInput(TypedDict, total=False):
    # The Auth0 id of a user, or uuid of another identity
    id: str

    # The email address of a user
    email: str

    # The name of the user. Will be ignored, but allowed so GET data can be round-tripped.
    name: str

class IdentityInput(RequiredIdentityInput, OptionalIdentityInput):
    pass
