"""
FIX 4.4 InstrmtMDReqGrp Component

This module contains the Pydantic model for the InstrmtMDReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class InstrmtMDReqGrp(TradeModel):
    """
    FIX 4.4 InstrmtMDReqGrp Component
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
    Instrument: str = Field(None)
    UndInstrmtGrp: Optional[str] = Field(None)
    InstrmtLegGrp: Optional[str] = Field(None)


class NoRelatedSym(TradeModel):
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

    NoRelatedSyms: List[NoRelatedSym] = Field(default_factory=list)
