"""
FIX 4.4 ExecCollGrp Component

This module contains the Pydantic model for the ExecCollGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class ExecCollGrp(FIXMessageBase):
    """
    FIX 4.4 ExecCollGrp Component
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
    execID: Optional[str] = Field(None, description='', alias='17')


class NoExecs(FIXMessageBase):
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
    execID: Optional[int] = Field(None, description='', alias='124')

    noExecss: List[NoExecs] = Field(default_factory=list)
