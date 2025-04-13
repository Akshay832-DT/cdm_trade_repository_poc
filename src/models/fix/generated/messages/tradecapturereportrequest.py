from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.instrumentextension import InstrumentExtensionComponent
from src.models.fix.generated.components.financingdetails import FinancingDetailsComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.trdcapdtgrp import TrdCapDtGrpComponent

class TradeCaptureReportRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    TradeRequestID: str = Field(..., description='', alias='568')
    TradeRequestType: int = Field(..., description='', alias='569')
    SubscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    TradeReportID: Optional[str] = Field(None, description='', alias='571')
    SecondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')
    ExecID: Optional[str] = Field(None, description='', alias='17')
    ExecType: Optional[str] = Field(None, description='', alias='150')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    MatchStatus: Optional[str] = Field(None, description='', alias='573')
    TrdType: Optional[int] = Field(None, description='', alias='828')
    TrdSubType: Optional[int] = Field(None, description='', alias='829')
    TransferReason: Optional[str] = Field(None, description='', alias='830')
    SecondaryTrdType: Optional[int] = Field(None, description='', alias='855')
    TradeLinkID: Optional[str] = Field(None, description='', alias='820')
    TrdMatchID: Optional[str] = Field(None, description='', alias='880')
    ClearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    TimeBracket: Optional[str] = Field(None, description='', alias='943')
    Side: Optional[str] = Field(None, description='', alias='54')
    MultiLegReportingType: Optional[str] = Field(None, description='', alias='442')
    TradeInputSource: Optional[str] = Field(None, description='', alias='578')
    TradeInputDevice: Optional[str] = Field(None, description='', alias='579')
    ResponseTransportType: Optional[int] = Field(None, description='', alias='725')
    ResponseDestination: Optional[str] = Field(None, description='', alias='726')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='InstrumentExtension component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    TrdCapDtGrp: Optional[TrdCapDtGrpComponent] = Field(None, description='TrdCapDtGrp component')

