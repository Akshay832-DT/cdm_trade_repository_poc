"""FIX message model for MassQuoteAcknowledgement (b).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.parties import PartiesComponent
from ..components.quotsetackgrp import QuotSetAckGrpComponent

class MassQuoteAcknowledgementMessage(FIXMessageBase):
    """FIX message model for MassQuoteAcknowledgement."""

    MsgType: str = Field("b", alias="35")

    QuoteReqID: Optional[str] = Field(None, alias='131', description='')
    QuoteID: Optional[str] = Field(None, alias='117', description='')
    QuoteStatus: int = Field(..., alias='297', description='')
    QuoteRejectReason: Optional[int] = Field(None, alias='300', description='')
    QuoteResponseLevel: Optional[int] = Field(None, alias='301', description='')
    QuoteType: Optional[int] = Field(None, alias='537', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    QuotSetAckGrp: Optional[QuotSetAckGrpComponent] = Field(None, description='')

