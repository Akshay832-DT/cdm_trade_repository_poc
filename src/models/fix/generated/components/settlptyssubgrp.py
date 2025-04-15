"""
FIX Component Model - SettlPtysSubGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoSettlPartySubIDsGroup(FIXComponentBase):

    """FIX Group - NoSettlPartySubIDs"""

    SettlPartySubID: Optional[str] = Field(None, alias='785', description='')
    SettlPartySubIDType: Optional[int] = Field(None, alias='786', description='')



class SettlPtysSubGrpComponent(FIXComponentBase):
    """FIX Component - SettlPtysSubGrp"""


