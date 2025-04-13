from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestampsComponent
from src.models.fix.generated.components.trdinstrmtleggrp import TrdInstrmtLegGrpComponent
from src.models.fix.generated.components.trdallocgrp import TrdAllocGrpComponent

class TradeCaptureReportAck(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    TradeReportID: str = Field(..., description='', alias='571')
    TradeReportTransType: Optional[int] = Field(None, description='', alias='487')
    TradeReportType: Optional[int] = Field(None, description='', alias='856')
    TrdType: Optional[int] = Field(None, description='', alias='828')
    TrdSubType: Optional[int] = Field(None, description='', alias='829')
    SecondaryTrdType: Optional[int] = Field(None, description='', alias='855')
    TransferReason: Optional[str] = Field(None, description='', alias='830')
    ExecType: str = Field(..., description='', alias='150')
    TradeReportRefID: Optional[str] = Field(None, description='', alias='572')
    SecondaryTradeReportRefID: Optional[str] = Field(None, description='', alias='881')
    TrdRptStatus: Optional[int] = Field(None, description='', alias='939')
    TradeReportRejectReason: Optional[int] = Field(None, description='', alias='751')
    SecondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')
    SubscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    TradeLinkID: Optional[str] = Field(None, description='', alias='820')
    TrdMatchID: Optional[str] = Field(None, description='', alias='880')
    ExecID: Optional[str] = Field(None, description='', alias='17')
    SecondaryExecID: Optional[str] = Field(None, description='', alias='527')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    ResponseTransportType: Optional[int] = Field(None, description='', alias='725')
    ResponseDestination: Optional[str] = Field(None, description='', alias='726')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    ClearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    OrderCapacity: Optional[str] = Field(None, description='', alias='528')
    OrderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    CustOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    PositionEffect: Optional[str] = Field(None, description='', alias='77')
    PreallocMethod: Optional[str] = Field(None, description='', alias='591')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    TrdRegTimestamps: Optional[TrdRegTimestampsComponent] = Field(None, description='TrdRegTimestamps component')
    TrdInstrmtLegGrp: Optional[TrdInstrmtLegGrpComponent] = Field(None, description='TrdInstrmtLegGrp component')
    TrdAllocGrp: Optional[TrdAllocGrpComponent] = Field(None, description='TrdAllocGrp component')

