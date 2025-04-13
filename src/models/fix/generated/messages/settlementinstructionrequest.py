from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent

class SettlementInstructionRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    SettlInstReqID: str = Field(..., description='', alias='791')
    TransactTime: datetime = Field(..., description='', alias='60')
    AllocAccount: Optional[str] = Field(None, description='', alias='79')
    AllocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    Side: Optional[str] = Field(None, description='', alias='54')
    Product: Optional[int] = Field(None, description='', alias='460')
    SecurityType: Optional[str] = Field(None, description='', alias='167')
    CFICode: Optional[str] = Field(None, description='', alias='461')
    EffectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    LastUpdateTime: Optional[datetime] = Field(None, description='', alias='779')
    StandInstDbType: Optional[int] = Field(None, description='', alias='169')
    StandInstDbName: Optional[str] = Field(None, description='', alias='170')
    StandInstDbID: Optional[str] = Field(None, description='', alias='171')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')

