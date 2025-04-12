"""
FIX 4.4 SettlInstGrp Component

This module contains the Pydantic model for the SettlInstGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class SettlInstGrp(TradeModel):
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
    SettlInstID: Optional[str] = Field(None, description='', alias='162')
    SettlInstTransType: Optional[str] = Field(None, description='', alias='163')
    SettlInstRefID: Optional[str] = Field(None, description='', alias='214')
    Side: Optional[str] = Field(None, description='', alias='54')
    Product: Optional[int] = Field(None, description='', alias='460')
    SecurityType: Optional[str] = Field(None, description='', alias='167')
    CFICode: Optional[str] = Field(None, description='', alias='461')
    EffectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    LastUpdateTime: Optional[datetime] = Field(None, description='', alias='779')
    PaymentMethod: Optional[int] = Field(None, description='', alias='492')
    PaymentRef: Optional[str] = Field(None, description='', alias='476')
    CardHolderName: Optional[str] = Field(None, description='', alias='488')
    CardNumber: Optional[str] = Field(None, description='', alias='489')
    CardStartDate: Optional[date] = Field(None, description='', alias='503')
    CardExpDate: Optional[date] = Field(None, description='', alias='490')
    CardIssNum: Optional[str] = Field(None, description='', alias='491')
    PaymentDate: Optional[date] = Field(None, description='', alias='504')
    PaymentRemitterID: Optional[str] = Field(None, description='', alias='505')
    Parties: Optional[str] = Field(None)
    SettlInstructionsData: Optional[str] = Field(None)


class NoSettlInst(TradeModel):
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
    SettlInstID: Optional[str] = Field(None, description='', alias='162')
    SettlInstTransType: Optional[str] = Field(None, description='', alias='163')
    SettlInstRefID: Optional[str] = Field(None, description='', alias='214')
    Side: Optional[str] = Field(None, description='', alias='54')
    Product: Optional[int] = Field(None, description='', alias='460')
    SecurityType: Optional[str] = Field(None, description='', alias='167')
    CFICode: Optional[str] = Field(None, description='', alias='461')
    EffectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    LastUpdateTime: Optional[datetime] = Field(None, description='', alias='779')
    PaymentMethod: Optional[int] = Field(None, description='', alias='492')
    PaymentRef: Optional[str] = Field(None, description='', alias='476')
    CardHolderName: Optional[str] = Field(None, description='', alias='488')
    CardNumber: Optional[str] = Field(None, description='', alias='489')
    CardStartDate: Optional[date] = Field(None, description='', alias='503')
    CardExpDate: Optional[date] = Field(None, description='', alias='490')
    CardIssNum: Optional[str] = Field(None, description='', alias='491')
    PaymentDate: Optional[date] = Field(None, description='', alias='504')
    PaymentRemitterID: Optional[str] = Field(None, description='', alias='505')

    NoSettlInsts: List[NoSettlInst] = Field(default_factory=list)
