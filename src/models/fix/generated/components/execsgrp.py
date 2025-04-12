"""
FIX 4.4 ExecsGrp Component

This module contains the Pydantic model for the ExecsGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class ExecsGrp(TradeModel):
    """
    FIX 4.4 ExecsGrp Component
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
    ExecID: Optional[str] = Field(None, description='', alias='17')


class NoExecs(TradeModel):
    """
    NoExecs group fields
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
    ExecID: Optional[str] = Field(None, description='', alias='17')

    NoExecss: List[NoExecs] = Field(default_factory=list)
