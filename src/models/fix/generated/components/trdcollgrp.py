"""
FIX 4.4 TrdCollGrp Component

This module contains the Pydantic model for the TrdCollGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class TrdCollGrp(TradeModel):
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
    TradeReportID: Optional[str] = Field(None, description='', alias='571')
    SecondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')


class NoTrades(TradeModel):
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
    TradeReportID: Optional[str] = Field(None, description='', alias='571')
    SecondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')

    NoTradess: List[NoTrades] = Field(default_factory=list)
