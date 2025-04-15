"""FIX message model for AllocationInstructionAck (P).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.allocackgrp import AllocAckGrpComponent
from ..components.parties import PartiesComponent

class AllocationInstructionAckMessage(FIXMessageBase):
    """FIX message model for AllocationInstructionAck."""

    MsgType: str = Field("P", alias="35")

    AllocID: str = Field(..., alias='70', description='')
    SecondaryAllocID: Optional[str] = Field(None, alias='793', description='')
    TradeDate: Optional[date] = Field(None, alias='75', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    AllocStatus: int = Field(..., alias='87', description='')
    AllocRejCode: Optional[int] = Field(None, alias='88', description='')
    AllocType: Optional[int] = Field(None, alias='626', description='')
    AllocIntermedReqType: Optional[int] = Field(None, alias='808', description='')
    MatchStatus: Optional[str] = Field(None, alias='573', description='')
    Product: Optional[int] = Field(None, alias='460', description='')
    SecurityType: Optional[str] = Field(None, alias='167', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    AllocAckGrp: Optional[AllocAckGrpComponent] = Field(None, description='')

