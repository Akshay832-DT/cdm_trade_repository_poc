from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent

class TradeCaptureReportRequestAck(FIXMessageBase):
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
    TotNumTradeReports: Optional[int] = Field(None, description='', alias='748')
    TradeRequestResult: int = Field(..., description='', alias='749')
    TradeRequestStatus: int = Field(..., description='', alias='750')
    MultiLegReportingType: Optional[str] = Field(None, description='', alias='442')
    ResponseTransportType: Optional[int] = Field(None, description='', alias='725')
    ResponseDestination: Optional[str] = Field(None, description='', alias='726')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')

