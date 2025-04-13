from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class TradingSessionStatus(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    tradsesreqid: Optional[str] = Field(None, description='', alias='335')
    tradingsessionid: str = Field(..., description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    tradsesmethod: Optional[int] = Field(None, description='', alias='338')
    tradsesmode: Optional[int] = Field(None, description='', alias='339')
    unsolicitedindicator: Optional[bool] = Field(None, description='', alias='325')
    tradsesstatus: int = Field(..., description='', alias='340')
    tradsesstatusrejreason: Optional[int] = Field(None, description='', alias='567')
    tradsesstarttime: Optional[datetime] = Field(None, description='', alias='341')
    tradsesopentime: Optional[datetime] = Field(None, description='', alias='342')
    tradsespreclosetime: Optional[datetime] = Field(None, description='', alias='343')
    tradsesclosetime: Optional[datetime] = Field(None, description='', alias='344')
    tradsesendtime: Optional[datetime] = Field(None, description='', alias='345')
    totalvolumetraded: Optional[float] = Field(None, description='', alias='387')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')

