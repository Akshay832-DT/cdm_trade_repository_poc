"""
FIX 4.4 TrdCollGrp Component

This module contains the Pydantic model for the TrdCollGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoTradesGroup(FIXComponentBase):
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


class TrdCollGrpComponent(FIXComponentBase):
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
    
    NoTrades: Optional[int] = Field(None, description='Number of NoTrades entries', alias='')
    NoTrades_items: List[NoTradesGroup] = Field(default_factory=list)
