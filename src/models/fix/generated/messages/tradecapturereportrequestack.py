"""FIX message model for TradeCaptureReportRequestAck (AQ).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class TradeCaptureReportRequestAckMessage(FIXMessageBase):
    """FIX message model for TradeCaptureReportRequestAck."""

    MsgType: str = Field("AQ", alias="35")

    TradeRequestID: str = Field(..., alias='568', description='')
    TradeRequestType: int = Field(..., alias='569', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    TotNumTradeReports: Optional[int] = Field(None, alias='748', description='')
    TradeRequestResult: int = Field(..., alias='749', description='')
    TradeRequestStatus: int = Field(..., alias='750', description='')
    MultiLegReportingType: Optional[str] = Field(None, alias='442', description='')
    ResponseTransportType: Optional[int] = Field(None, alias='725', description='')
    ResponseDestination: Optional[str] = Field(None, alias='726', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Instrument: InstrumentComponent = Field(..., description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')

