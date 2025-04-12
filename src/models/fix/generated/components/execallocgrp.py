"""
FIX 4.4 ExecAllocGrp Component

This module contains the Pydantic model for the ExecAllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class ExecAllocGrp(FIXMessageBase):
    """
    FIX 4.4 ExecAllocGrp Component
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
    lastQty: Optional[float] = Field(None, description='', alias='32')
    execID: Optional[str] = Field(None, description='', alias='17')
    secondaryExecID: Optional[str] = Field(None, description='', alias='527')
    lastPx: Optional[float] = Field(None, description='', alias='31')
    lastParPx: Optional[float] = Field(None, description='', alias='669')
    lastCapacity: Optional[str] = Field(None, description='', alias='29')


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
    lastQty: Optional[int] = Field(None, description='', alias='124')
    execID: Optional[int] = Field(None, description='', alias='124')
    secondaryExecID: Optional[int] = Field(None, description='', alias='124')
    lastPx: Optional[int] = Field(None, description='', alias='124')
    lastParPx: Optional[int] = Field(None, description='', alias='124')
    lastCapacity: Optional[int] = Field(None, description='', alias='124')

    noExecss: List[NoExecs] = Field(default_factory=list)
