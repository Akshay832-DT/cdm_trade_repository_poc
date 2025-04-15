"""FIX message model for TradeCaptureReportRequest (AD).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.instrumentextension import InstrumentExtensionComponent
from ..components.parties import PartiesComponent
from ..components.trdcapdtgrp import TrdCapDtGrpComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class TradeCaptureReportRequestMessage(FIXMessageBase):
    """FIX message model for TradeCaptureReportRequest."""

    MsgType: str = Field("AD", alias="35")

    TradeRequestID: str = Field(..., alias='568', description='')
    TradeRequestType: int = Field(..., alias='569', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    TradeReportID: Optional[str] = Field(None, alias='571', description='')
    SecondaryTradeReportID: Optional[str] = Field(None, alias='818', description='')
    ExecID: Optional[str] = Field(None, alias='17', description='')
    ExecType: Optional[str] = Field(None, alias='150', description='')
    OrderID: Optional[str] = Field(None, alias='37', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    MatchStatus: Optional[str] = Field(None, alias='573', description='')
    TrdType: Optional[int] = Field(None, alias='828', description='')
    TrdSubType: Optional[int] = Field(None, alias='829', description='')
    TransferReason: Optional[str] = Field(None, alias='830', description='')
    SecondaryTrdType: Optional[int] = Field(None, alias='855', description='')
    TradeLinkID: Optional[str] = Field(None, alias='820', description='')
    TrdMatchID: Optional[str] = Field(None, alias='880', description='')
    ClearingBusinessDate: Optional[date] = Field(None, alias='715', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    TimeBracket: Optional[str] = Field(None, alias='943', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    MultiLegReportingType: Optional[str] = Field(None, alias='442', description='')
    TradeInputSource: Optional[str] = Field(None, alias='578', description='')
    TradeInputDevice: Optional[str] = Field(None, alias='579', description='')
    ResponseTransportType: Optional[int] = Field(None, alias='725', description='')
    ResponseDestination: Optional[str] = Field(None, alias='726', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    TrdCapDtGrp: Optional[TrdCapDtGrpComponent] = Field(None, description='')

