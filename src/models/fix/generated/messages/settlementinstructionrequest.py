from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties

class SettlementInstructionRequest(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    settlinstreqid: str = Field(..., description='', alias='791')
    transacttime: datetime = Field(..., description='', alias='60')
    allocaccount: Optional[str] = Field(None, description='', alias='79')
    allocacctidsource: Optional[int] = Field(None, description='', alias='661')
    side: Optional[str] = Field(None, description='', alias='54')
    product: Optional[int] = Field(None, description='', alias='460')
    securitytype: Optional[str] = Field(None, description='', alias='167')
    cficode: Optional[str] = Field(None, description='', alias='461')
    effectivetime: Optional[datetime] = Field(None, description='', alias='168')
    expiretime: Optional[datetime] = Field(None, description='', alias='126')
    lastupdatetime: Optional[datetime] = Field(None, description='', alias='779')
    standinstdbtype: Optional[int] = Field(None, description='', alias='169')
    standinstdbname: Optional[str] = Field(None, description='', alias='170')
    standinstdbid: Optional[str] = Field(None, description='', alias='171')
    parties: Optional[Parties] = Field(None, description='Parties component')

