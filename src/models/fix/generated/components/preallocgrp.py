"""
FIX Component Model - PreAllocGrp
"""

from ..base import FIXComponentBase
from .nestedparties import NestedPartiesComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoAllocsGroup(FIXComponentBase):

    """FIX Group - NoAllocs"""

    AllocAccount: Optional[str] = Field(None, alias='79', description='')
    AllocAcctIDSource: Optional[int] = Field(None, alias='661', description='')
    AllocSettlCurrency: Optional[str] = Field(None, alias='736', description='')
    IndividualAllocID: Optional[str] = Field(None, alias='467', description='')
    AllocQty: Optional[float] = Field(None, alias='80', description='')
    NestedParties: Optional[NestedPartiesComponent] = Field(None, description='')



class PreAllocGrpComponent(FIXComponentBase):
    """FIX Component - PreAllocGrp"""


