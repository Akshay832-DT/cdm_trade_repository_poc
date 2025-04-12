"""
FIX 4.4 PositionAmountData Component

This module contains the Pydantic model for the PositionAmountData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class PositionAmountData(TradeModel):
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
    PosAmtType: Optional[str] = Field(None, description='', alias='707')
    PosAmt: Optional[float] = Field(None, description='', alias='708')


class NoPosAmt(TradeModel):
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
    PosAmtType: Optional[str] = Field(None, description='', alias='707')
    PosAmt: Optional[float] = Field(None, description='', alias='708')

    NoPosAmts: List[NoPosAmt] = Field(default_factory=list)
