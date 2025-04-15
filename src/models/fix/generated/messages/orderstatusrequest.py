"""FIX message model for OrderStatusRequest (H).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrument import InstrumentComponent
from ..components.parties import PartiesComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class OrderStatusRequestMessage(FIXMessageBase):
    """FIX message model for OrderStatusRequest."""

    MsgType: str = Field("H", alias="35")

    OrderID: Optional[str] = Field(None, alias='37', description='')
    ClOrdID: str = Field(..., alias='11', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    ClOrdLinkID: Optional[str] = Field(None, alias='583', description='')
    OrdStatusReqID: Optional[str] = Field(None, alias='790', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    Side: str = Field(..., alias='54', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    Instrument: InstrumentComponent = Field(..., description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')

