"""
FIX 4.4 DiscretionInstructions Component

This module contains the Pydantic model for the DiscretionInstructions component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class DiscretionInstructionsComponent(FIXComponentBase):
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
    
    DiscretionInst: Optional[str] = Field(None, description='', alias='388')
    DiscretionOffsetValue: Optional[float] = Field(None, description='', alias='389')
    DiscretionMoveType: Optional[int] = Field(None, description='', alias='841')
    DiscretionOffsetType: Optional[int] = Field(None, description='', alias='842')
    DiscretionLimitType: Optional[int] = Field(None, description='', alias='843')
    DiscretionRoundDirection: Optional[int] = Field(None, description='', alias='844')
    DiscretionScope: Optional[int] = Field(None, description='', alias='846')
