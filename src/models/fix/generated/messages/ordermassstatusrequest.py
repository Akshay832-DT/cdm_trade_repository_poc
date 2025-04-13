from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrumentComponent

class OrderMassStatusRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    MassStatusReqID: str = Field(..., description='', alias='584')
    MassStatusReqType: int = Field(..., description='', alias='585')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    Side: Optional[str] = Field(None, description='', alias='54')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='UnderlyingInstrument component')

