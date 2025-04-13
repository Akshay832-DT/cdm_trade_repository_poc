from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent

class RegistrationInstructionsResponse(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    RegistID: str = Field(..., description='', alias='513')
    RegistTransType: str = Field(..., description='', alias='514')
    RegistRefID: str = Field(..., description='', alias='508')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    RegistStatus: str = Field(..., description='', alias='506')
    RegistRejReasonCode: Optional[int] = Field(None, description='', alias='507')
    RegistRejReasonText: Optional[str] = Field(None, description='', alias='496')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')

