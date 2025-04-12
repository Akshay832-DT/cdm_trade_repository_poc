"""
FIX 4.4 SettlInstGrp Component

This module contains the Pydantic model for the SettlInstGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class SettlInstGrp(FIXMessageBase):
    """
    FIX 4.4 SettlInstGrp Component
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    settlInstID: Optional[str] = Field(None, description='', alias='162')
    settlInstTransType: Optional[str] = Field(None, description='', alias='163')
    settlInstRefID: Optional[str] = Field(None, description='', alias='214')
    side: Optional[str] = Field(None, description='', alias='54')
    product: Optional[int] = Field(None, description='', alias='460')
    securityType: Optional[str] = Field(None, description='', alias='167')
    cFICode: Optional[str] = Field(None, description='', alias='461')
    effectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    expireTime: Optional[datetime] = Field(None, description='', alias='126')
    lastUpdateTime: Optional[datetime] = Field(None, description='', alias='779')
    paymentMethod: Optional[int] = Field(None, description='', alias='492')
    paymentRef: Optional[str] = Field(None, description='', alias='476')
    cardHolderName: Optional[str] = Field(None, description='', alias='488')
    cardNumber: Optional[str] = Field(None, description='', alias='489')
    cardStartDate: Optional[date] = Field(None, description='', alias='503')
    cardExpDate: Optional[date] = Field(None, description='', alias='490')
    cardIssNum: Optional[str] = Field(None, description='', alias='491')
    paymentDate: Optional[date] = Field(None, description='', alias='504')
    paymentRemitterID: Optional[str] = Field(None, description='', alias='505')
    parties: Optional[str] = Field(None)
    settlInstructionsData: Optional[str] = Field(None)


class NoSettlInst(FIXMessageBase):
    """
    NoSettlInst group fields
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    settlInstID: Optional[int] = Field(None, description='', alias='778')
    settlInstTransType: Optional[int] = Field(None, description='', alias='778')
    settlInstRefID: Optional[int] = Field(None, description='', alias='778')
    side: Optional[int] = Field(None, description='', alias='778')
    product: Optional[int] = Field(None, description='', alias='778')
    securityType: Optional[int] = Field(None, description='', alias='778')
    cFICode: Optional[int] = Field(None, description='', alias='778')
    effectiveTime: Optional[int] = Field(None, description='', alias='778')
    expireTime: Optional[int] = Field(None, description='', alias='778')
    lastUpdateTime: Optional[int] = Field(None, description='', alias='778')
    paymentMethod: Optional[int] = Field(None, description='', alias='778')
    paymentRef: Optional[int] = Field(None, description='', alias='778')
    cardHolderName: Optional[int] = Field(None, description='', alias='778')
    cardNumber: Optional[int] = Field(None, description='', alias='778')
    cardStartDate: Optional[int] = Field(None, description='', alias='778')
    cardExpDate: Optional[int] = Field(None, description='', alias='778')
    cardIssNum: Optional[int] = Field(None, description='', alias='778')
    paymentDate: Optional[int] = Field(None, description='', alias='778')
    paymentRemitterID: Optional[int] = Field(None, description='', alias='778')

    noSettlInsts: List[NoSettlInst] = Field(default_factory=list)
