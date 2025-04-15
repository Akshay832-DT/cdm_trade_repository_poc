"""
FIX Component Model - OrdAllocGrp
"""

from ..base import FIXComponentBase
from .nestedparties2 import NestedParties2Component
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoOrdersGroup(FIXComponentBase):

    """FIX Group - NoOrders"""

    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    OrderID: Optional[str] = Field(None, alias='37', description='')
    SecondaryOrderID: Optional[str] = Field(None, alias='198', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    ListID: Optional[str] = Field(None, alias='66', description='')
    OrderQty: Optional[float] = Field(None, alias='38', description='')
    OrderAvgPx: Optional[float] = Field(None, alias='799', description='')
    OrderBookingQty: Optional[float] = Field(None, alias='800', description='')
    NestedParties2: Optional[NestedParties2Component] = Field(None, description='')



class OrdAllocGrpComponent(FIXComponentBase):
    """FIX Component - OrdAllocGrp"""


