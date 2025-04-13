from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.allocackgrp import AllocAckGrp

class AllocationReportAck(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    allocreportid: str = Field(..., description='', alias='755')
    allocid: str = Field(..., description='', alias='70')
    secondaryallocid: Optional[str] = Field(None, description='', alias='793')
    tradedate: Optional[date] = Field(None, description='', alias='75')
    transacttime: datetime = Field(..., description='', alias='60')
    allocstatus: int = Field(..., description='', alias='87')
    allocrejcode: Optional[int] = Field(None, description='', alias='88')
    allocreporttype: Optional[int] = Field(None, description='', alias='794')
    allocintermedreqtype: Optional[int] = Field(None, description='', alias='808')
    matchstatus: Optional[str] = Field(None, description='', alias='573')
    product: Optional[int] = Field(None, description='', alias='460')
    securitytype: Optional[str] = Field(None, description='', alias='167')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    allocackgrp: Optional[AllocAckGrp] = Field(None, description='AllocAckGrp component')

