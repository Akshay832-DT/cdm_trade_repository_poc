"""
FIX 4.4 BidDescReqGrp Component

This module contains the Pydantic model for the BidDescReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoBidDescriptors(FIXMessageBase):
    """
    NoBidDescriptors group fields
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
    
    bidDescriptorType: Optional[int] = Field(None, description='', alias='399')
    bidDescriptor: Optional[str] = Field(None, description='', alias='400')
    sideValueInd: Optional[int] = Field(None, description='', alias='401')
    liquidityValue: Optional[float] = Field(None, description='', alias='404')
    liquidityNumSecurities: Optional[int] = Field(None, description='', alias='441')
    liquidityPctLow: Optional[float] = Field(None, description='', alias='402')
    liquidityPctHigh: Optional[float] = Field(None, description='', alias='403')
    eFPTrackingError: Optional[float] = Field(None, description='', alias='405')
    fairValue: Optional[float] = Field(None, description='', alias='406')
    outsideIndexPct: Optional[float] = Field(None, description='', alias='407')
    valueOfFutures: Optional[float] = Field(None, description='', alias='408')


class BidDescReqGrp(FIXMessageBase):
    """
    FIX 4.4 BidDescReqGrp Component
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
    
    noBidDescriptors: Optional[int] = Field(None, description='Number of NoBidDescriptors entries', alias='398')
    noBidDescriptors_items: List[NoBidDescriptors] = Field(default_factory=list)
