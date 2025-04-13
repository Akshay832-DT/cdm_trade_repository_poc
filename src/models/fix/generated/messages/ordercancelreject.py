from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class OrderCancelReject(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    orderid: str = Field(..., description='', alias='37')
    secondaryorderid: Optional[str] = Field(None, description='', alias='198')
    secondaryclordid: Optional[str] = Field(None, description='', alias='526')
    clordid: str = Field(..., description='', alias='11')
    clordlinkid: Optional[str] = Field(None, description='', alias='583')
    origclordid: str = Field(..., description='', alias='41')
    ordstatus: str = Field(..., description='', alias='39')
    workingindicator: Optional[bool] = Field(None, description='', alias='636')
    origordmodtime: Optional[datetime] = Field(None, description='', alias='586')
    listid: Optional[str] = Field(None, description='', alias='66')
    account: Optional[str] = Field(None, description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    accounttype: Optional[int] = Field(None, description='', alias='581')
    tradeoriginationdate: Optional[date] = Field(None, description='', alias='229')
    tradedate: Optional[date] = Field(None, description='', alias='75')
    transacttime: Optional[datetime] = Field(None, description='', alias='60')
    cxlrejresponseto: str = Field(..., description='', alias='434')
    cxlrejreason: Optional[int] = Field(None, description='', alias='102')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')

