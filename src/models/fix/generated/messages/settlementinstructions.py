from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.settlinstgrp import SettlInstGrp

class SettlementInstructions(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    settlinstmsgid: str = Field(..., description='', alias='777')
    settlinstreqid: Optional[str] = Field(None, description='', alias='791')
    settlinstmode: str = Field(..., description='', alias='160')
    settlinstreqrejcode: Optional[int] = Field(None, description='', alias='792')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    clordid: Optional[str] = Field(None, description='', alias='11')
    transacttime: datetime = Field(..., description='', alias='60')
    settlinstgrp: Optional[SettlInstGrp] = Field(None, description='SettlInstGrp component')

