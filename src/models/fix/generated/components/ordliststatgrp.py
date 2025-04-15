"""
FIX Component Model - OrdListStatGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoOrdersGroup(FIXComponentBase):

    """FIX Group - NoOrders"""

    ClOrdID: str = Field(alias='11', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    CumQty: float = Field(alias='14', description='')
    OrdStatus: str = Field(alias='39', description='')
    WorkingIndicator: Optional[bool] = Field(None, alias='636', description='')
    LeavesQty: float = Field(alias='151', description='')
    CxlQty: float = Field(alias='84', description='')
    AvgPx: float = Field(alias='6', description='')
    OrdRejReason: Optional[int] = Field(None, alias='103', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')



class OrdListStatGrpComponent(FIXComponentBase):
    """FIX Component - OrdListStatGrp"""


