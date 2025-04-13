"""
FIX 4.4 BidCompReqGrp Component

This module contains the Pydantic model for the BidCompReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoBidComponents(FIXMessageBase):
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
    side: Optional[str] = Field(None, description='', alias='54')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    netGrossInd: Optional[int] = Field(None, description='', alias='430')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')


class BidCompReqGrp(FIXMessageBase):
    """
    FIX 4.4 BidCompReqGrp Component
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
