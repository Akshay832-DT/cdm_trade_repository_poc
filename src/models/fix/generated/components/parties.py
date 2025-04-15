"""
FIX Component Model - Parties
"""

from ..base import FIXComponentBase
from .ptyssubgrp import PtysSubGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoPartyIDsGroup(FIXComponentBase):

    """FIX Group - NoPartyIDs"""

    PartyID: Optional[str] = Field(None, alias='448', description='')
    PartyIDSource: Optional[str] = Field(None, alias='447', description='')
    PartyRole: Optional[int] = Field(None, alias='452', description='')
    PtysSubGrp: Optional[PtysSubGrpComponent] = Field(None, description='')



class PartiesComponent(FIXComponentBase):
    """FIX Component - Parties"""


