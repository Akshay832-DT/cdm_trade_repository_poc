"""FIX message model for ListStatus (N).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.ordliststatgrp import OrdListStatGrpComponent

class ListStatusMessage(FIXMessageBase):
    """FIX message model for ListStatus."""

    MsgType: str = Field("N", alias="35")

    ListID: str = Field(..., alias='66', description='')
    ListStatusType: int = Field(..., alias='429', description='')
    NoRpts: int = Field(..., alias='82', description='')
    ListOrderStatus: int = Field(..., alias='431', description='')
    RptSeq: int = Field(..., alias='83', description='')
    ListStatusText: Optional[str] = Field(None, alias='444', description='')
    EncodedListStatusTextLen: Optional[int] = Field(None, alias='445', description='')
    EncodedListStatusText: Optional[str] = Field(None, alias='446', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')
    TotNoOrders: int = Field(..., alias='68', description='')
    LastFragment: Optional[bool] = Field(None, alias='893', description='')
    OrdListStatGrp: OrdListStatGrpComponent = Field(..., description='')

