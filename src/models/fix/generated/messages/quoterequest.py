from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.quotreqgrp import QuotReqGrp

class QuoteRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    quotereqid: str = Field(..., description='', alias='131')
    rfqreqid: Optional[str] = Field(None, description='', alias='644')
    clordid: Optional[str] = Field(None, description='', alias='11')
    ordercapacity: Optional[str] = Field(None, description='', alias='528')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    quotreqgrp: QuotReqGrp = Field(..., description='QuotReqGrp component')

