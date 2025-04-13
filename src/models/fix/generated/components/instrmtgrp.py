"""
FIX 4.4 InstrmtGrp Component

This module contains the Pydantic model for the InstrmtGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument


class NoRelatedSym(FIXMessageBase):
    """
    NoRelatedSym group fields
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
    


class InstrmtGrp(FIXMessageBase):
    """
    FIX 4.4 InstrmtGrp Component
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
    
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    noRelatedSym: Optional[int] = Field(None, description='Number of NoRelatedSym entries', alias='146')
    noRelatedSym_items: List[NoRelatedSym] = Field(default_factory=list)
