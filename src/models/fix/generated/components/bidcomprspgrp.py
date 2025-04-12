"""
FIX 4.4 BidCompRspGrp Component

This module contains the Pydantic model for the BidCompRspGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from .commissiondata import CommissionData


class NoBidComponents(TradeModel):
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
    ListID: Optional[str] = Field(None, description='', alias='66')
    Country: Optional[str] = Field(None, description='', alias='421')
    Side: Optional[str] = Field(None, description='', alias='54')
    Price: Optional[float] = Field(None, description='', alias='44')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    FairValue: Optional[float] = Field(None, description='', alias='406')
    NetGrossInd: Optional[int] = Field(None, description='', alias='430')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    CommissionData: Optional[CommissionData] = None


class BidCompRspGrp(TradeModel):
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
    
    # Count field for the number of bid components
    NoBidComponents: Optional[int] = Field(None, description='Number of bid components', alias='420')
    
    # List of bid components
    NoBidComponents_Items: List[NoBidComponents] = Field(default_factory=list)
