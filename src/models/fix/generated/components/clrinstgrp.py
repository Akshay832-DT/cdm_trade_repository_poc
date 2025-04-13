"""
FIX 4.4 ClrInstGrp Component

This module contains the Pydantic model for the ClrInstGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoClearingInstructions(FIXMessageBase):
    """
    NoClearingInstructions group fields
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
    
    clearingInstruction: Optional[int] = Field(None, description='', alias='577')


class ClrInstGrp(FIXMessageBase):
    """
    FIX 4.4 ClrInstGrp Component
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
    
    noClearingInstructions: Optional[int] = Field(None, description='Number of NoClearingInstructions entries', alias='576')
    noClearingInstructions_items: List[NoClearingInstructions] = Field(default_factory=list)
