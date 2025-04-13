from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.quotcxlentriesgrp import QuotCxlEntriesGrp

class QuoteCancel(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    quotereqid: Optional[str] = Field(None, description='', alias='131')
    quoteid: str = Field(..., description='', alias='117')
    quotecanceltype: int = Field(..., description='', alias='298')
    quoteresponselevel: Optional[int] = Field(None, description='', alias='301')
    account: Optional[str] = Field(None, description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    accounttype: Optional[int] = Field(None, description='', alias='581')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    parties: Optional[Parties] = Field(None, description='Parties component')
    quotcxlentriesgrp: Optional[QuotCxlEntriesGrp] = Field(None, description='QuotCxlEntriesGrp component')

