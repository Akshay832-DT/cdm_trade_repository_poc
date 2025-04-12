"""
FIX 4.4 SecAltIDGrp Component

This module contains the Pydantic model for the SecAltIDGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class SecAltIDGrp(TradeModel):
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
    SecurityAltID: Optional[str] = Field(None, description='', alias='455')
    SecurityAltIDSource: Optional[str] = Field(None, description='', alias='456')


class NoSecurityAltID(TradeModel):
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
    SecurityAltID: Optional[str] = Field(None, description='', alias='455')
    SecurityAltIDSource: Optional[str] = Field(None, description='', alias='456')

    NoSecurityAltIDs: List[NoSecurityAltID] = Field(default_factory=list)
