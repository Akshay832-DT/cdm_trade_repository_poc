from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrument

class DerivativeSecurityListRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    securityreqid: str = Field(..., description='', alias='320')
    securitylistrequesttype: int = Field(..., description='', alias='559')
    securitysubtype: Optional[str] = Field(None, description='', alias='762')
    currency: Optional[str] = Field(None, description='', alias='15')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    subscriptionrequesttype: Optional[str] = Field(None, description='', alias='263')
    underlyinginstrument: Optional[UnderlyingInstrument] = Field(None, description='UnderlyingInstrument component')

