"""
FIX Component Model - NstdPtys2SubGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoNested2PartySubIDsGroup(FIXComponentBase):

    """FIX Group - NoNested2PartySubIDs"""

    Nested2PartySubID: Optional[str] = Field(None, alias='760', description='')
    Nested2PartySubIDType: Optional[int] = Field(None, alias='807', description='')



class NstdPtys2SubGrpComponent(FIXComponentBase):
    """FIX Component - NstdPtys2SubGrp"""


