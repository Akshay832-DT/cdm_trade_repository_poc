"""
FIX 4.4 UndSecAltIDGrp Component

This module contains the Pydantic model for the UndSecAltIDGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class UndSecAltIDGrp(TradeModel):
    """
    FIX 4.4 UndSecAltIDGrp Component
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
    UnderlyingSecurityAltID: Optional[str] = Field(None, description='', alias='458')
    UnderlyingSecurityAltIDSource: Optional[str] = Field(None, description='', alias='459')


class NoUnderlyingSecurityAltID(TradeModel):
    """
    NoUnderlyingSecurityAltID group fields
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
    UnderlyingSecurityAltID: Optional[str] = Field(None, description='', alias='458')
    UnderlyingSecurityAltIDSource: Optional[str] = Field(None, description='', alias='459')

    NoUnderlyingSecurityAltIDs: List[NoUnderlyingSecurityAltID] = Field(default_factory=list)
