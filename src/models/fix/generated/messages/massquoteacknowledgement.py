from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.quotsetackgrp import QuotSetAckGrpComponent

class MassQuoteAcknowledgement(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    QuoteReqID: Optional[str] = Field(None, description='', alias='131')
    QuoteID: Optional[str] = Field(None, description='', alias='117')
    QuoteStatus: int = Field(..., description='', alias='297')
    QuoteRejectReason: Optional[int] = Field(None, description='', alias='300')
    QuoteResponseLevel: Optional[int] = Field(None, description='', alias='301')
    QuoteType: Optional[int] = Field(None, description='', alias='537')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    QuotSetAckGrp: Optional[QuotSetAckGrpComponent] = Field(None, description='QuotSetAckGrp component')

