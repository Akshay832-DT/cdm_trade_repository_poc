from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.quotsetgrp import QuotSetGrpComponent

class MassQuote(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    QuoteReqID: Optional[str] = Field(None, description='', alias='131')
    QuoteID: str = Field(..., description='', alias='117')
    QuoteType: Optional[int] = Field(None, description='', alias='537')
    QuoteResponseLevel: Optional[int] = Field(None, description='', alias='301')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    DefBidSize: Optional[float] = Field(None, description='', alias='293')
    DefOfferSize: Optional[float] = Field(None, description='', alias='294')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    QuotSetGrp: QuotSetGrpComponent = Field(..., description='QuotSetGrp component')

