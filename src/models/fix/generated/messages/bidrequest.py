from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.biddescreqgrp import BidDescReqGrpComponent
from src.models.fix.generated.components.bidcompreqgrp import BidCompReqGrpComponent

class BidRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    BidID: Optional[str] = Field(None, description='', alias='390')
    ClientBidID: str = Field(..., description='', alias='391')
    BidRequestTransType: str = Field(..., description='', alias='374')
    ListName: Optional[str] = Field(None, description='', alias='392')
    TotNoRelatedSym: int = Field(..., description='', alias='393')
    BidType: int = Field(..., description='', alias='394')
    NumTickets: Optional[int] = Field(None, description='', alias='395')
    Currency: Optional[str] = Field(None, description='', alias='15')
    SideValue1: Optional[float] = Field(None, description='', alias='396')
    SideValue2: Optional[float] = Field(None, description='', alias='397')
    LiquidityIndType: Optional[int] = Field(None, description='', alias='409')
    WtAverageLiquidity: Optional[float] = Field(None, description='', alias='410')
    ExchangeForPhysical: Optional[bool] = Field(None, description='', alias='411')
    OutMainCntryUIndex: Optional[float] = Field(None, description='', alias='412')
    CrossPercent: Optional[float] = Field(None, description='', alias='413')
    ProgRptReqs: Optional[int] = Field(None, description='', alias='414')
    ProgPeriodInterval: Optional[int] = Field(None, description='', alias='415')
    IncTaxInd: Optional[int] = Field(None, description='', alias='416')
    ForexReq: Optional[bool] = Field(None, description='', alias='121')
    NumBidders: Optional[int] = Field(None, description='', alias='417')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    BidTradeType: str = Field(..., description='', alias='418')
    BasisPxType: str = Field(..., description='', alias='419')
    StrikeTime: Optional[datetime] = Field(None, description='', alias='443')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    BidDescReqGrp: Optional[BidDescReqGrpComponent] = Field(None, description='BidDescReqGrp component')
    BidCompReqGrp: Optional[BidCompReqGrpComponent] = Field(None, description='BidCompReqGrp component')

