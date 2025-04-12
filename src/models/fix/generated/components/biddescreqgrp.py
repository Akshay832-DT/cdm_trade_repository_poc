"""
FIX 4.4 BidDescReqGrp Component

This module contains the Pydantic model for the BidDescReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class BidDescReqGrp(TradeModel):
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
    BidDescriptorType: Optional[int] = Field(None, description='', alias='399')
    BidDescriptor: Optional[str] = Field(None, description='', alias='400')
    SideValueInd: Optional[int] = Field(None, description='', alias='401')
    LiquidityValue: Optional[float] = Field(None, description='', alias='404')
    LiquidityNumSecurities: Optional[int] = Field(None, description='', alias='441')
    LiquidityPctLow: Optional[float] = Field(None, description='', alias='402')
    LiquidityPctHigh: Optional[float] = Field(None, description='', alias='403')
    EFPTrackingError: Optional[float] = Field(None, description='', alias='405')
    FairValue: Optional[float] = Field(None, description='', alias='406')
    OutsideIndexPct: Optional[float] = Field(None, description='', alias='407')
    ValueOfFutures: Optional[float] = Field(None, description='', alias='408')


class NoBidDescriptors(TradeModel):
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
    BidDescriptorType: Optional[int] = Field(None, description='', alias='399')
    BidDescriptor: Optional[str] = Field(None, description='', alias='400')
    SideValueInd: Optional[int] = Field(None, description='', alias='401')
    LiquidityValue: Optional[float] = Field(None, description='', alias='404')
    LiquidityNumSecurities: Optional[int] = Field(None, description='', alias='441')
    LiquidityPctLow: Optional[float] = Field(None, description='', alias='402')
    LiquidityPctHigh: Optional[float] = Field(None, description='', alias='403')
    EFPTrackingError: Optional[float] = Field(None, description='', alias='405')
    FairValue: Optional[float] = Field(None, description='', alias='406')
    OutsideIndexPct: Optional[float] = Field(None, description='', alias='407')
    ValueOfFutures: Optional[float] = Field(None, description='', alias='408')

    NoBidDescriptorss: List[NoBidDescriptors] = Field(default_factory=list)
