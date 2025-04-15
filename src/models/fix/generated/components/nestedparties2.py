"""
FIX Component Model - NestedParties2
"""

from ..base import FIXComponentBase
from .nstdptys2subgrp import NstdPtys2SubGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoNested2PartyIDsGroup(FIXComponentBase):

    """FIX Group - NoNested2PartyIDs"""

    Nested2PartyID: Optional[str] = Field(None, alias='757', description='')
    Nested2PartyIDSource: Optional[str] = Field(None, alias='758', description='')
    Nested2PartyRole: Optional[int] = Field(None, alias='759', description='')
    NstdPtys2SubGrp: Optional[NstdPtys2SubGrpComponent] = Field(None, description='')



class NestedParties2Component(FIXComponentBase):
    """FIX Component - NestedParties2"""


