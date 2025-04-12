"""
FIX 4.4 TrdgSesGrp Component

This module contains the Pydantic model for the TrdgSesGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class TrdgSesGrp(FIXMessageBase):
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
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')


class NoTradingSessions(FIXMessageBase):
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
    tradingSessionID: Optional[int] = Field(None, description='', alias='386')
    tradingSessionSubID: Optional[int] = Field(None, description='', alias='386')

    noTradingSessionss: List[NoTradingSessions] = Field(default_factory=list)
