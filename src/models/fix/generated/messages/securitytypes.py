from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.sectypesgrp import SecTypesGrpComponent

class SecurityTypes(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    SecurityReqID: str = Field(..., description='', alias='320')
    SecurityResponseID: str = Field(..., description='', alias='322')
    SecurityResponseType: int = Field(..., description='', alias='323')
    TotNoSecurityTypes: Optional[int] = Field(None, description='', alias='557')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    SubscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    SecTypesGrp: Optional[SecTypesGrpComponent] = Field(None, description='SecTypesGrp component')

