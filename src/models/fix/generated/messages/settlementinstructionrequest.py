"""FIX message model for SettlementInstructionRequest (AV).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.parties import PartiesComponent

class SettlementInstructionRequestMessage(FIXMessageBase):
    """FIX message model for SettlementInstructionRequest."""

    MsgType: str = Field("AV", alias="35")

    SettlInstReqID: str = Field(..., alias='791', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    AllocAccount: Optional[str] = Field(None, alias='79', description='')
    AllocAcctIDSource: Optional[int] = Field(None, alias='661', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    Product: Optional[int] = Field(None, alias='460', description='')
    SecurityType: Optional[str] = Field(None, alias='167', description='')
    CFICode: Optional[str] = Field(None, alias='461', description='')
    EffectiveTime: Optional[datetime] = Field(None, alias='168', description='')
    ExpireTime: Optional[datetime] = Field(None, alias='126', description='')
    LastUpdateTime: Optional[datetime] = Field(None, alias='779', description='')
    StandInstDbType: Optional[int] = Field(None, alias='169', description='')
    StandInstDbName: Optional[str] = Field(None, alias='170', description='')
    StandInstDbID: Optional[str] = Field(None, alias='171', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')

