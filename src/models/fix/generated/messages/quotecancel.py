"""FIX message model for QuoteCancel (Z).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.parties import PartiesComponent
from ..components.quotcxlentriesgrp import QuotCxlEntriesGrpComponent

class QuoteCancelMessage(FIXMessageBase):
    """FIX message model for QuoteCancel."""

    MsgType: str = Field("Z", alias="35")

    QuoteReqID: Optional[str] = Field(None, alias='131', description='')
    QuoteID: str = Field(..., alias='117', description='')
    QuoteCancelType: int = Field(..., alias='298', description='')
    QuoteResponseLevel: Optional[int] = Field(None, alias='301', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    QuotCxlEntriesGrp: Optional[QuotCxlEntriesGrpComponent] = Field(None, description='')

