"""
FIX 4.4 MiscFeesGrp Component

This module contains the Pydantic model for the MiscFeesGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class MiscFeesGrp(TradeModel):
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
    MiscFeeAmt: Optional[float] = Field(None, description='', alias='137')
    MiscFeeCurr: Optional[str] = Field(None, description='', alias='138')
    MiscFeeType: Optional[str] = Field(None, description='', alias='139')
    MiscFeeBasis: Optional[int] = Field(None, description='', alias='891')


class NoMiscFees(TradeModel):
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
    MiscFeeAmt: Optional[float] = Field(None, description='', alias='137')
    MiscFeeCurr: Optional[str] = Field(None, description='', alias='138')
    MiscFeeType: Optional[str] = Field(None, description='', alias='139')
    MiscFeeBasis: Optional[int] = Field(None, description='', alias='891')

    NoMiscFeess: List[NoMiscFees] = Field(default_factory=list)
