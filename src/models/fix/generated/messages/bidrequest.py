from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.biddescreqgrp import BidDescReqGrp
from src.models.fix.generated.components.bidcompreqgrp import BidCompReqGrp

class BidRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    bidid: Optional[str] = Field(None, description='', alias='390')
    clientbidid: str = Field(..., description='', alias='391')
    bidrequesttranstype: str = Field(..., description='', alias='374')
    listname: Optional[str] = Field(None, description='', alias='392')
    totnorelatedsym: int = Field(..., description='', alias='393')
    bidtype: int = Field(..., description='', alias='394')
    numtickets: Optional[int] = Field(None, description='', alias='395')
    currency: Optional[str] = Field(None, description='', alias='15')
    sidevalue1: Optional[float] = Field(None, description='', alias='396')
    sidevalue2: Optional[float] = Field(None, description='', alias='397')
    liquidityindtype: Optional[int] = Field(None, description='', alias='409')
    wtaverageliquidity: Optional[float] = Field(None, description='', alias='410')
    exchangeforphysical: Optional[bool] = Field(None, description='', alias='411')
    outmaincntryuindex: Optional[float] = Field(None, description='', alias='412')
    crosspercent: Optional[float] = Field(None, description='', alias='413')
    progrptreqs: Optional[int] = Field(None, description='', alias='414')
    progperiodinterval: Optional[int] = Field(None, description='', alias='415')
    inctaxind: Optional[int] = Field(None, description='', alias='416')
    forexreq: Optional[bool] = Field(None, description='', alias='121')
    numbidders: Optional[int] = Field(None, description='', alias='417')
    tradedate: Optional[date] = Field(None, description='', alias='75')
    bidtradetype: str = Field(..., description='', alias='418')
    basispxtype: str = Field(..., description='', alias='419')
    striketime: Optional[datetime] = Field(None, description='', alias='443')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    biddescreqgrp: Optional[BidDescReqGrp] = Field(None, description='BidDescReqGrp component')
    bidcompreqgrp: Optional[BidCompReqGrp] = Field(None, description='BidCompReqGrp component')

