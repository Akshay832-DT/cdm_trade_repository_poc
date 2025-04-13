from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.ordallocgrp import OrdAllocGrp

class ConfirmationRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    confirmreqid: str = Field(..., description='', alias='859')
    confirmtype: int = Field(..., description='', alias='773')
    allocid: Optional[str] = Field(None, description='', alias='70')
    secondaryallocid: Optional[str] = Field(None, description='', alias='793')
    individualallocid: Optional[str] = Field(None, description='', alias='467')
    transacttime: datetime = Field(..., description='', alias='60')
    allocaccount: Optional[str] = Field(None, description='', alias='79')
    allocacctidsource: Optional[int] = Field(None, description='', alias='661')
    allocaccounttype: Optional[int] = Field(None, description='', alias='798')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    ordallocgrp: Optional[OrdAllocGrp] = Field(None, description='OrdAllocGrp component')

