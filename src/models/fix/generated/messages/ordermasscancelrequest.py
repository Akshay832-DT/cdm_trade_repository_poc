from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrument

class OrderMassCancelRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    clordid: str = Field(..., description='', alias='11')
    secondaryclordid: Optional[str] = Field(None, description='', alias='526')
    masscancelrequesttype: str = Field(..., description='', alias='530')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    side: Optional[str] = Field(None, description='', alias='54')
    transacttime: datetime = Field(..., description='', alias='60')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    underlyinginstrument: Optional[UnderlyingInstrument] = Field(None, description='UnderlyingInstrument component')

