from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.quotsetackgrp import QuotSetAckGrp

class MassQuoteAcknowledgement(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    quotereqid: Optional[str] = Field(None, description='', alias='131')
    quoteid: Optional[str] = Field(None, description='', alias='117')
    quotestatus: int = Field(..., description='', alias='297')
    quoterejectreason: Optional[int] = Field(None, description='', alias='300')
    quoteresponselevel: Optional[int] = Field(None, description='', alias='301')
    quotetype: Optional[int] = Field(None, description='', alias='537')
    account: Optional[str] = Field(None, description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    accounttype: Optional[int] = Field(None, description='', alias='581')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    quotsetackgrp: Optional[QuotSetAckGrp] = Field(None, description='QuotSetAckGrp component')

