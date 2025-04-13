from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrumentComponent

class OrderMassCancelRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    ClOrdID: str = Field(..., description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    MassCancelRequestType: str = Field(..., description='', alias='530')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    Side: Optional[str] = Field(None, description='', alias='54')
    TransactTime: datetime = Field(..., description='', alias='60')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='UnderlyingInstrument component')

