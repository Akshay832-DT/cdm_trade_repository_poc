"""
FIX Component Model - NstdPtys3SubGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoNested3PartySubIDsGroup(FIXComponentBase):

    """FIX Group - NoNested3PartySubIDs"""

    Nested3PartySubID: Optional[str] = Field(None, alias='953', description='')
    Nested3PartySubIDType: Optional[int] = Field(None, alias='954', description='')



class NstdPtys3SubGrpComponent(FIXComponentBase):
    """FIX Component - NstdPtys3SubGrp"""


