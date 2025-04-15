"""
FIX Component Model - AllocAckGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoAllocsGroup(FIXComponentBase):

    """FIX Group - NoAllocs"""

    AllocAccount: Optional[str] = Field(None, alias='79', description='')
    AllocAcctIDSource: Optional[int] = Field(None, alias='661', description='')
    AllocPrice: Optional[float] = Field(None, alias='366', description='')
    IndividualAllocID: Optional[str] = Field(None, alias='467', description='')
    IndividualAllocRejCode: Optional[int] = Field(None, alias='776', description='')
    AllocText: Optional[str] = Field(None, alias='161', description='')
    EncodedAllocTextLen: Optional[int] = Field(None, alias='360', description='')
    EncodedAllocText: Optional[str] = Field(None, alias='361', description='')



class AllocAckGrpComponent(FIXComponentBase):
    """FIX Component - AllocAckGrp"""


