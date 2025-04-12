"""
FIX 4.4 AttrbGrp Component

This module contains the Pydantic model for the AttrbGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class AttrbGrp(FIXMessageBase):
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
    instrAttribType: Optional[int] = Field(None, description='', alias='871')
    instrAttribValue: Optional[str] = Field(None, description='', alias='872')


class NoInstrAttrib(FIXMessageBase):
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
    instrAttribType: Optional[int] = Field(None, description='', alias='870')
    instrAttribValue: Optional[int] = Field(None, description='', alias='870')

    noInstrAttribs: List[NoInstrAttrib] = Field(default_factory=list)
