"""
FIX 4.4 BidCompRspGrp Component

This module contains the Pydantic model for the BidCompRspGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.commissiondata import CommissionData


class NoBidComponents(BaseModel):
    """
    NoBidComponents group fields
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
    
    listID: Optional[str] = Field(None, description='', alias='66')
    country: Optional[str] = Field(None, description='', alias='421')
    side: Optional[str] = Field(None, description='', alias='54')
    price: Optional[float] = Field(None, description='', alias='44')
    priceType: Optional[int] = Field(None, description='', alias='423')
    fairValue: Optional[float] = Field(None, description='', alias='406')
    netGrossInd: Optional[int] = Field(None, description='', alias='430')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    commissionData: Optional[CommissionData] = Field(None, description='CommissionData component')


class BidCompRspGrp(BaseModel):
    """
    FIX 4.4 BidCompRspGrp Component
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
    
    noBidComponents: Optional[int] = Field(None, description='Number of NoBidComponents entries', alias='420')
    noBidComponents_items: List[NoBidComponents] = Field(default_factory=list)
