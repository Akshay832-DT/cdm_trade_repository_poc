"""
FIX 4.4 AttrbGrp Component

This module contains the Pydantic model for the AttrbGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class AttrbGrp(TradeModel):
    """
    FIX 4.4 AttrbGrp Component
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
    InstrAttribType: Optional[int] = Field(None, description='', alias='871')
    InstrAttribValue: Optional[str] = Field(None, description='', alias='872')


class NoInstrAttrib(TradeModel):
    """
    NoInstrAttrib group fields
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
    InstrAttribType: Optional[int] = Field(None, description='', alias='871')
    InstrAttribValue: Optional[str] = Field(None, description='', alias='872')

    NoInstrAttribs: List[NoInstrAttrib] = Field(default_factory=list)
