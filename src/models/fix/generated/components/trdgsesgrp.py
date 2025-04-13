"""
FIX 4.4 TrdgSesGrp Component

This module contains the Pydantic model for the TrdgSesGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoTradingSessionsGroup(FIXComponentBase):
    """
    NoTradingSessions group fields
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
    
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')


class TrdgSesGrpComponent(FIXComponentBase):
    """
    FIX 4.4 TrdgSesGrp Component
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
    
    NoTradingSessions: Optional[int] = Field(None, description='Number of NoTradingSessions entries', alias='')
    NoTradingSessions_items: List[NoTradingSessionsGroup] = Field(default_factory=list)
