"""
FIX 4.4 PosUndInstrmtGrp Component

This module contains the Pydantic model for the PosUndInstrmtGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrument


class NoUnderlyings(FIXMessageBase):
    """
    NoUnderlyings group fields
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
    
    underlyingSettlPrice: float = Field(..., description='', alias='732')
    underlyingSettlPriceType: int = Field(..., description='', alias='733')


class PosUndInstrmtGrp(FIXMessageBase):
    """
    FIX 4.4 PosUndInstrmtGrp Component
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
    
    underlyingInstrument: Optional[UnderlyingInstrument] = Field(None, description='UnderlyingInstrument component')
    noUnderlyings: Optional[int] = Field(None, description='Number of NoUnderlyings entries', alias='711')
    noUnderlyings_items: List[NoUnderlyings] = Field(default_factory=list)
