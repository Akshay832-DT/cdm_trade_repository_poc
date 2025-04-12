"""
FIX 4.4 PosUndInstrmtGrp Component

This module contains the Pydantic model for the PosUndInstrmtGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class PosUndInstrmtGrp(TradeModel):
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
    UnderlyingSettlPrice: float = Field(None, description='', alias='732')
    UnderlyingSettlPriceType: int = Field(None, description='', alias='733')
    UnderlyingInstrument: Optional[str] = Field(None)


class NoUnderlyings(TradeModel):
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
    UnderlyingSettlPrice: float = Field(None, description='', alias='732')
    UnderlyingSettlPriceType: int = Field(None, description='', alias='733')

    NoUnderlyingss: List[NoUnderlyings] = Field(default_factory=list)
