"""FIX message model for OrderMassCancelReport (r).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.affectedordgrp import AffectedOrdGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.underlyinginstrument import UnderlyingInstrumentComponent

class OrderMassCancelReportMessage(FIXMessageBase):
    """FIX message model for OrderMassCancelReport."""

    MsgType: str = Field("r", alias="35")

    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    OrderID: str = Field(..., alias='37', description='')
    SecondaryOrderID: Optional[str] = Field(None, alias='198', description='')
    MassCancelRequestType: str = Field(..., alias='530', description='')
    MassCancelResponse: str = Field(..., alias='531', description='')
    MassCancelRejectReason: Optional[str] = Field(None, alias='532', description='')
    TotalAffectedOrders: Optional[int] = Field(None, alias='533', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    AffectedOrdGrp: Optional[AffectedOrdGrpComponent] = Field(None, description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')

