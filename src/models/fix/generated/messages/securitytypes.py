from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.sectypesgrp import SecTypesGrp

class SecurityTypes(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    securityreqid: str = Field(..., description='', alias='320')
    securityresponseid: str = Field(..., description='', alias='322')
    securityresponsetype: int = Field(..., description='', alias='323')
    totnosecuritytypes: Optional[int] = Field(None, description='', alias='557')
    lastfragment: Optional[bool] = Field(None, description='', alias='893')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    tradingsessionid: Optional[str] = Field(None, description='', alias='336')
    tradingsessionsubid: Optional[str] = Field(None, description='', alias='625')
    subscriptionrequesttype: Optional[str] = Field(None, description='', alias='263')
    sectypesgrp: Optional[SecTypesGrp] = Field(None, description='SecTypesGrp component')

