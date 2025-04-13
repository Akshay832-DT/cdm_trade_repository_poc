"""
FIX 4.4 MiscFeesGrp Component

This module contains the Pydantic model for the MiscFeesGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoMiscFees(FIXMessageBase):
    """
    NoMiscFees group fields
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
    
    miscFeeAmt: Optional[float] = Field(None, description='', alias='137')
    miscFeeCurr: Optional[str] = Field(None, description='', alias='138')
    miscFeeType: Optional[str] = Field(None, description='', alias='139')
    miscFeeBasis: Optional[int] = Field(None, description='', alias='891')


class MiscFeesGrp(FIXMessageBase):
    """
    FIX 4.4 MiscFeesGrp Component
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
    
    noMiscFees: Optional[int] = Field(None, description='Number of NoMiscFees entries', alias='136')
    noMiscFees_items: List[NoMiscFees] = Field(default_factory=list)
