"""FIX message model for BidRequest (k).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.bidcompreqgrp import BidCompReqGrpComponent
from ..components.biddescreqgrp import BidDescReqGrpComponent

class BidRequestMessage(FIXMessageBase):
    """FIX message model for BidRequest."""

    MsgType: str = Field("k", alias="35")

    BidID: Optional[str] = Field(None, alias='390', description='')
    ClientBidID: str = Field(..., alias='391', description='')
    BidRequestTransType: str = Field(..., alias='374', description='')
    ListName: Optional[str] = Field(None, alias='392', description='')
    TotNoRelatedSym: int = Field(..., alias='393', description='')
    BidType: int = Field(..., alias='394', description='')
    NumTickets: Optional[int] = Field(None, alias='395', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    SideValue1: Optional[float] = Field(None, alias='396', description='')
    SideValue2: Optional[float] = Field(None, alias='397', description='')
    LiquidityIndType: Optional[int] = Field(None, alias='409', description='')
    WtAverageLiquidity: Optional[float] = Field(None, alias='410', description='')
    ExchangeForPhysical: Optional[bool] = Field(None, alias='411', description='')
    OutMainCntryUIndex: Optional[float] = Field(None, alias='412', description='')
    CrossPercent: Optional[float] = Field(None, alias='413', description='')
    ProgRptReqs: Optional[int] = Field(None, alias='414', description='')
    ProgPeriodInterval: Optional[int] = Field(None, alias='415', description='')
    IncTaxInd: Optional[int] = Field(None, alias='416', description='')
    ForexReq: Optional[bool] = Field(None, alias='121', description='')
    NumBidders: Optional[int] = Field(None, alias='417', description='')
    TradeDate: Optional[date] = Field(None, alias='75', description='')
    BidTradeType: str = Field(..., alias='418', description='')
    BasisPxType: str = Field(..., alias='419', description='')
    StrikeTime: Optional[datetime] = Field(None, alias='443', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    BidDescReqGrp: Optional[BidDescReqGrpComponent] = Field(None, description='')
    BidCompReqGrp: Optional[BidCompReqGrpComponent] = Field(None, description='')

