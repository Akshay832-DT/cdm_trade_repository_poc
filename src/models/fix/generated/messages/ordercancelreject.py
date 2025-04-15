"""FIX message model for OrderCancelReject (9).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase

class OrderCancelRejectMessage(FIXMessageBase):
    """FIX message model for OrderCancelReject."""

    MsgType: str = Field("9", alias="35")

    OrderID: str = Field(..., alias='37', description='')
    SecondaryOrderID: Optional[str] = Field(None, alias='198', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    ClOrdID: str = Field(..., alias='11', description='')
    ClOrdLinkID: Optional[str] = Field(None, alias='583', description='')
    OrigClOrdID: str = Field(..., alias='41', description='')
    OrdStatus: str = Field(..., alias='39', description='')
    WorkingIndicator: Optional[bool] = Field(None, alias='636', description='')
    OrigOrdModTime: Optional[datetime] = Field(None, alias='586', description='')
    ListID: Optional[str] = Field(None, alias='66', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    TradeOriginationDate: Optional[date] = Field(None, alias='229', description='')
    TradeDate: Optional[date] = Field(None, alias='75', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')
    CxlRejResponseTo: str = Field(..., alias='434', description='')
    CxlRejReason: Optional[int] = Field(None, alias='102', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')

