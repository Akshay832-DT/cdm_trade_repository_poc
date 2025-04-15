"""FIX message model for ConfirmationRequest (BH).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.ordallocgrp import OrdAllocGrpComponent

class ConfirmationRequestMessage(FIXMessageBase):
    """FIX message model for ConfirmationRequest."""

    MsgType: str = Field("BH", alias="35")

    ConfirmReqID: str = Field(..., alias='859', description='')
    ConfirmType: int = Field(..., alias='773', description='')
    AllocID: Optional[str] = Field(None, alias='70', description='')
    SecondaryAllocID: Optional[str] = Field(None, alias='793', description='')
    IndividualAllocID: Optional[str] = Field(None, alias='467', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    AllocAccount: Optional[str] = Field(None, alias='79', description='')
    AllocAcctIDSource: Optional[int] = Field(None, alias='661', description='')
    AllocAccountType: Optional[int] = Field(None, alias='798', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    OrdAllocGrp: Optional[OrdAllocGrpComponent] = Field(None, description='')

