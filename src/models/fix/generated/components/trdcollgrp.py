"""
FIX 4.4 TrdCollGrp Component

This module contains the Pydantic model for the TrdCollGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoTrades(FIXMessageBase):
    """
    NoTrades group fields
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
    
    tradeReportID: Optional[str] = Field(None, description='', alias='571')
    secondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')


class TrdCollGrp(FIXMessageBase):
    """
    FIX 4.4 TrdCollGrp Component
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
    
    noTrades: Optional[int] = Field(None, description='Number of NoTrades entries', alias='897')
    noTrades_items: List[NoTrades] = Field(default_factory=list)
