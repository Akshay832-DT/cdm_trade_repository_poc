"""
FIX Component Model - NestedParties3
"""

from ..base import FIXComponentBase
from .nstdptys3subgrp import NstdPtys3SubGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoNested3PartyIDsGroup(FIXComponentBase):

    """FIX Group - NoNested3PartyIDs"""

    Nested3PartyID: Optional[str] = Field(None, alias='949', description='')
    Nested3PartyIDSource: Optional[str] = Field(None, alias='950', description='')
    Nested3PartyRole: Optional[int] = Field(None, alias='951', description='')
    NstdPtys3SubGrp: Optional[NstdPtys3SubGrpComponent] = Field(None, description='')



class NestedParties3Component(FIXComponentBase):
    """FIX Component - NestedParties3"""


