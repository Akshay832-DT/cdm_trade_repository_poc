from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.ordallocgrp import OrdAllocGrpComponent

class ConfirmationRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    ConfirmReqID: str = Field(..., description='', alias='859')
    ConfirmType: int = Field(..., description='', alias='773')
    AllocID: Optional[str] = Field(None, description='', alias='70')
    SecondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    IndividualAllocID: Optional[str] = Field(None, description='', alias='467')
    TransactTime: datetime = Field(..., description='', alias='60')
    AllocAccount: Optional[str] = Field(None, description='', alias='79')
    AllocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    AllocAccountType: Optional[int] = Field(None, description='', alias='798')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    OrdAllocGrp: Optional[OrdAllocGrpComponent] = Field(None, description='OrdAllocGrp component')

