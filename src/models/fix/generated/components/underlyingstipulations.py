"""
FIX 4.4 UnderlyingStipulations Component

This module contains the Pydantic model for the UnderlyingStipulations component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoUnderlyingStips(FIXMessageBase):
    """
    NoUnderlyingStips group fields
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
    
    underlyingStipType: Optional[str] = Field(None, description='', alias='888')
    underlyingStipValue: Optional[str] = Field(None, description='', alias='889')


class UnderlyingStipulations(FIXMessageBase):
    """
    FIX 4.4 UnderlyingStipulations Component
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
    
    noUnderlyingStips: Optional[int] = Field(None, description='Number of NoUnderlyingStips entries', alias='887')
    noUnderlyingStips_items: List[NoUnderlyingStips] = Field(default_factory=list)
