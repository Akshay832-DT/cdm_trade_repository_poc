"""
FIX Component Model - SettlParties
"""

from ..base import FIXComponentBase
from .settlptyssubgrp import SettlPtysSubGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoSettlPartyIDsGroup(FIXComponentBase):

    """FIX Group - NoSettlPartyIDs"""

    SettlPartyID: Optional[str] = Field(None, alias='782', description='')
    SettlPartyIDSource: Optional[str] = Field(None, alias='783', description='')
    SettlPartyRole: Optional[int] = Field(None, alias='784', description='')
    SettlPtysSubGrp: Optional[SettlPtysSubGrpComponent] = Field(None, description='')



class SettlPartiesComponent(FIXComponentBase):
    """FIX Component - SettlParties"""


