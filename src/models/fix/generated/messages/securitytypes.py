"""FIX message model for SecurityTypes (w).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.sectypesgrp import SecTypesGrpComponent

class SecurityTypesMessage(FIXMessageBase):
    """FIX message model for SecurityTypes."""

    MsgType: str = Field("w", alias="35")

    SecurityReqID: str = Field(..., alias='320', description='')
    SecurityResponseID: str = Field(..., alias='322', description='')
    SecurityResponseType: int = Field(..., alias='323', description='')
    TotNoSecurityTypes: Optional[int] = Field(None, alias='557', description='')
    LastFragment: Optional[bool] = Field(None, alias='893', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    SecTypesGrp: Optional[SecTypesGrpComponent] = Field(None, description='')

