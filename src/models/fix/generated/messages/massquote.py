"""FIX message model for MassQuote (i).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.parties import PartiesComponent
from ..components.quotsetgrp import QuotSetGrpComponent

class MassQuoteMessage(FIXMessageBase):
    """FIX message model for MassQuote."""

    MsgType: str = Field("i", alias="35")

    QuoteReqID: Optional[str] = Field(None, alias='131', description='')
    QuoteID: str = Field(..., alias='117', description='')
    QuoteType: Optional[int] = Field(None, alias='537', description='')
    QuoteResponseLevel: Optional[int] = Field(None, alias='301', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    DefBidSize: Optional[float] = Field(None, alias='293', description='')
    DefOfferSize: Optional[float] = Field(None, alias='294', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    QuotSetGrp: QuotSetGrpComponent = Field(..., description='')

