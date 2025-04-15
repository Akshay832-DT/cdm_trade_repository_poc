"""
FIX Component Model - PtysSubGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoPartySubIDsGroup(FIXComponentBase):

    """FIX Group - NoPartySubIDs"""

    PartySubID: Optional[str] = Field(None, alias='523', description='')
    PartySubIDType: Optional[int] = Field(None, alias='803', description='')



class PtysSubGrpComponent(FIXComponentBase):
    """FIX Component - PtysSubGrp"""


