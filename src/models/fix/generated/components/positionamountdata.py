"""
FIX 4.4 PositionAmountData Component

This module contains the Pydantic model for the PositionAmountData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class PositionAmountData(FIXMessageBase):
    """
    FIX 4.4 PositionAmountData Component
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
    posAmtType: Optional[str] = Field(None, description='', alias='707')
    posAmt: Optional[float] = Field(None, description='', alias='708')


class NoPosAmt(FIXMessageBase):
    """
    NoPosAmt group fields
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
    posAmtType: Optional[int] = Field(None, description='', alias='753')
    posAmt: Optional[int] = Field(None, description='', alias='753')

    noPosAmts: List[NoPosAmt] = Field(default_factory=list)
