"""FIX message model for OrderCancelRequest (F).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrument import InstrumentComponent
from ..components.orderqtydata import OrderQtyDataComponent
from ..components.parties import PartiesComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class OrderCancelRequestMessage(FIXMessageBase):
    """FIX message model for OrderCancelRequest."""

    MsgType: str = Field("F", alias="35")

    OrigClOrdID: str = Field(..., alias='41', description='')
    OrderID: Optional[str] = Field(None, alias='37', description='')
    ClOrdID: str = Field(..., alias='11', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    ClOrdLinkID: Optional[str] = Field(None, alias='583', description='')
    ListID: Optional[str] = Field(None, alias='66', description='')
    OrigOrdModTime: Optional[datetime] = Field(None, alias='586', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    Side: str = Field(..., alias='54', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    ComplianceID: Optional[str] = Field(None, alias='376', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    Instrument: InstrumentComponent = Field(..., description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    OrderQtyData: OrderQtyDataComponent = Field(..., description='')

