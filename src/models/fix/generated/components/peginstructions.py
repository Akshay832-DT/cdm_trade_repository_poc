"""
FIX 4.4 PegInstructions Component

This module contains the Pydantic model for the PegInstructions component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class PegInstructions(FIXMessageBase):
    """
    FIX 4.4 PegInstructions Component
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
    
    pegOffsetValue: Optional[float] = Field(None, description='', alias='211')
    pegMoveType: Optional[int] = Field(None, description='', alias='835')
    pegOffsetType: Optional[int] = Field(None, description='', alias='836')
    pegLimitType: Optional[int] = Field(None, description='', alias='837')
    pegRoundDirection: Optional[int] = Field(None, description='', alias='838')
    pegScope: Optional[int] = Field(None, description='', alias='840')
