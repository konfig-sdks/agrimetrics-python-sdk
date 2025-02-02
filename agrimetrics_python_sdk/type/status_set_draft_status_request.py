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

from agrimetrics_python_sdk.type.draft_status import DraftStatus

class RequiredStatusSetDraftStatusRequest(TypedDict):
    status: typing.Union[DraftStatus, typing.Optional[str]]

class OptionalStatusSetDraftStatusRequest(TypedDict, total=False):
    # Any notes added during review of the data set
    notes: str

class StatusSetDraftStatusRequest(RequiredStatusSetDraftStatusRequest, OptionalStatusSetDraftStatusRequest):
    pass
