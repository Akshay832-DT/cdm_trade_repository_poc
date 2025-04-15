"""
FIX Component Model - NestedParties
"""

from ..base import FIXComponentBase
from .nstdptyssubgrp import NstdPtysSubGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoNestedPartyIDsGroup(FIXComponentBase):

    """FIX Group - NoNestedPartyIDs"""

    NestedPartyID: Optional[str] = Field(None, alias='524', description='')
    NestedPartyIDSource: Optional[str] = Field(None, alias='525', description='')
    NestedPartyRole: Optional[int] = Field(None, alias='538', description='')
    NstdPtysSubGrp: Optional[NstdPtysSubGrpComponent] = Field(None, description='')



class NestedPartiesComponent(FIXComponentBase):
    """FIX Component - NestedParties"""


