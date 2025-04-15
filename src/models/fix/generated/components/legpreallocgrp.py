"""
FIX Component Model - LegPreAllocGrp
"""

from ..base import FIXComponentBase
from .nestedparties2 import NestedParties2Component
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoLegAllocsGroup(FIXComponentBase):

    """FIX Group - NoLegAllocs"""

    LegAllocAccount: Optional[str] = Field(None, alias='671', description='')
    LegIndividualAllocID: Optional[str] = Field(None, alias='672', description='')
    LegAllocQty: Optional[float] = Field(None, alias='673', description='')
    LegAllocAcctIDSource: Optional[str] = Field(None, alias='674', description='')
    LegSettlCurrency: Optional[str] = Field(None, alias='675', description='')
    NestedParties2: Optional[NestedParties2Component] = Field(None, description='')



class LegPreAllocGrpComponent(FIXComponentBase):
    """FIX Component - LegPreAllocGrp"""


