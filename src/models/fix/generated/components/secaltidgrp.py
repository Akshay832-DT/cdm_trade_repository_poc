"""
FIX 4.4 SecAltIDGrp Component

This module contains the Pydantic model for the SecAltIDGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class SecAltIDGrp(FIXMessageBase):
    """
    FIX 4.4 SecAltIDGrp Component
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
    securityAltID: Optional[str] = Field(None, description='', alias='455')
    securityAltIDSource: Optional[str] = Field(None, description='', alias='456')


class NoSecurityAltID(FIXMessageBase):
    """
    NoSecurityAltID group fields
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
    securityAltID: Optional[int] = Field(None, description='', alias='454')
    securityAltIDSource: Optional[int] = Field(None, description='', alias='454')

    noSecurityAltIDs: List[NoSecurityAltID] = Field(default_factory=list)
