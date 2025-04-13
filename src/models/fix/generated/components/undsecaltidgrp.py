"""
FIX 4.4 UndSecAltIDGrp Component

This module contains the Pydantic model for the UndSecAltIDGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoUnderlyingSecurityAltID(FIXMessageBase):
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
    
    underlyingSecurityAltID: Optional[str] = Field(None, description='', alias='458')
    underlyingSecurityAltIDSource: Optional[str] = Field(None, description='', alias='459')


class UndSecAltIDGrp(FIXMessageBase):
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
    
    noUnderlyingSecurityAltID: Optional[int] = Field(None, description='Number of NoUnderlyingSecurityAltID entries', alias='457')
    noUnderlyingSecurityAltID_items: List[NoUnderlyingSecurityAltID] = Field(default_factory=list)
