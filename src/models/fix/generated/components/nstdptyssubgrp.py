"""
FIX Component Model - NstdPtysSubGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoNestedPartySubIDsGroup(FIXComponentBase):

    """FIX Group - NoNestedPartySubIDs"""

    NestedPartySubID: Optional[str] = Field(None, alias='545', description='')
    NestedPartySubIDType: Optional[int] = Field(None, alias='805', description='')



class NstdPtysSubGrpComponent(FIXComponentBase):
    """FIX Component - NstdPtysSubGrp"""


