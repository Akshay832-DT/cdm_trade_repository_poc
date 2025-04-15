"""FIX message model for TradeCaptureReportAck (AR).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrument import InstrumentComponent
from ..components.trdallocgrp import TrdAllocGrpComponent
from ..components.trdinstrmtleggrp import TrdInstrmtLegGrpComponent
from ..components.trdregtimestamps import TrdRegTimestampsComponent

class TradeCaptureReportAckMessage(FIXMessageBase):
    """FIX message model for TradeCaptureReportAck."""

    MsgType: str = Field("AR", alias="35")

    TradeReportID: str = Field(..., alias='571', description='')
    TradeReportTransType: Optional[int] = Field(None, alias='487', description='')
    TradeReportType: Optional[int] = Field(None, alias='856', description='')
    TrdType: Optional[int] = Field(None, alias='828', description='')
    TrdSubType: Optional[int] = Field(None, alias='829', description='')
    SecondaryTrdType: Optional[int] = Field(None, alias='855', description='')
    TransferReason: Optional[str] = Field(None, alias='830', description='')
    ExecType: str = Field(..., alias='150', description='')
    TradeReportRefID: Optional[str] = Field(None, alias='572', description='')
    SecondaryTradeReportRefID: Optional[str] = Field(None, alias='881', description='')
    TrdRptStatus: Optional[int] = Field(None, alias='939', description='')
    TradeReportRejectReason: Optional[int] = Field(None, alias='751', description='')
    SecondaryTradeReportID: Optional[str] = Field(None, alias='818', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    TradeLinkID: Optional[str] = Field(None, alias='820', description='')
    TrdMatchID: Optional[str] = Field(None, alias='880', description='')
    ExecID: Optional[str] = Field(None, alias='17', description='')
    SecondaryExecID: Optional[str] = Field(None, alias='527', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')
    ResponseTransportType: Optional[int] = Field(None, alias='725', description='')
    ResponseDestination: Optional[str] = Field(None, alias='726', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    ClearingFeeIndicator: Optional[str] = Field(None, alias='635', description='')
    OrderCapacity: Optional[str] = Field(None, alias='528', description='')
    OrderRestrictions: Optional[List[str]] = Field(None, alias='529', description='')
    CustOrderCapacity: Optional[int] = Field(None, alias='582', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    PositionEffect: Optional[str] = Field(None, alias='77', description='')
    PreallocMethod: Optional[str] = Field(None, alias='591', description='')
    Instrument: InstrumentComponent = Field(..., description='')
    TrdRegTimestamps: Optional[TrdRegTimestampsComponent] = Field(None, description='')
    TrdInstrmtLegGrp: Optional[TrdInstrmtLegGrpComponent] = Field(None, description='')
    TrdAllocGrp: Optional[TrdAllocGrpComponent] = Field(None, description='')

