from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase

class OrderCancelReject(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    OrderID: str = Field(..., description='', alias='37')
    SecondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    ClOrdID: str = Field(..., description='', alias='11')
    ClOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    OrigClOrdID: str = Field(..., description='', alias='41')
    OrdStatus: str = Field(..., description='', alias='39')
    WorkingIndicator: Optional[bool] = Field(None, description='', alias='636')
    OrigOrdModTime: Optional[datetime] = Field(None, description='', alias='586')
    ListID: Optional[str] = Field(None, description='', alias='66')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    CxlRejResponseTo: str = Field(..., description='', alias='434')
    CxlRejReason: Optional[int] = Field(None, description='', alias='102')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')

