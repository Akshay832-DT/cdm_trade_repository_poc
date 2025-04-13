from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrument

class OrderMassStatusRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    massstatusreqid: str = Field(..., description='', alias='584')
    massstatusreqtype: int = Field(..., description='', alias='585')
    account: Optional[str] = Field(None, description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    side: Optional[str] = Field(None, description='', alias='54')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    underlyinginstrument: Optional[UnderlyingInstrument] = Field(None, description='UnderlyingInstrument component')

