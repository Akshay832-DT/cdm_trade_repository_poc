from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class TradingSessionStatusRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    tradsesreqid: str = Field(..., description='', alias='335')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    tradsesmethod: Optional[int] = Field(None, description='', alias='338')
    tradsesmode: Optional[int] = Field(None, description='', alias='339')
    subscriptionrequesttype: str = Field(..., description='', alias='263')

