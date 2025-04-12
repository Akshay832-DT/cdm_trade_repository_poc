"""
FIX 4.4 DiscretionInstructions Component

This module contains the Pydantic model for the DiscretionInstructions component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class DiscretionInstructions(FIXMessageBase):
    """
    FIX 4.4 DiscretionInstructions Component
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
    discretionInst: Optional[str] = Field(None, description='', alias='388')
    discretionOffsetValue: Optional[float] = Field(None, description='', alias='389')
    discretionMoveType: Optional[int] = Field(None, description='', alias='841')
    discretionOffsetType: Optional[int] = Field(None, description='', alias='842')
    discretionLimitType: Optional[int] = Field(None, description='', alias='843')
    discretionRoundDirection: Optional[int] = Field(None, description='', alias='844')
    discretionScope: Optional[int] = Field(None, description='', alias='846')
