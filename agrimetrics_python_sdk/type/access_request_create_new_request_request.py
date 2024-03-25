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


class RequiredAccessRequestCreateNewRequestRequest(TypedDict):
    # The ID of a dataset in the catalog
    dataSetId: str

    # ID for the entity which is requesting access.
    requestingEntityId: str

    # Free text message provided by the user when requesting access.
    requestMessage: str

class OptionalAccessRequestCreateNewRequestRequest(TypedDict, total=False):
    # Name of the user who requested access.
    requesterName: str

    # Contact email address for the user who requested access.
    requesterEmail: str

class AccessRequestCreateNewRequestRequest(RequiredAccessRequestCreateNewRequestRequest, OptionalAccessRequestCreateNewRequestRequest):
    pass
