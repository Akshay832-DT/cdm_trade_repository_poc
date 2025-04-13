"""
FIX 4.4 SettlInstGrp Component

This module contains the Pydantic model for the SettlInstGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.settlinstructionsdata import SettlInstructionsData


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
    
    parties: Optional[Parties] = Field(None, description='Parties component')
    settlInstructionsData: Optional[SettlInstructionsData] = Field(None, description='SettlInstructionsData component')
    noSettlInst: Optional[int] = Field(None, description='Number of NoSettlInst entries', alias='778')
    noSettlInst_items: List[NoSettlInst] = Field(default_factory=list)
