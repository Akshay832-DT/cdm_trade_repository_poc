"""
FIX 4.4 LegSecAltIDGrp Component

This module contains the Pydantic model for the LegSecAltIDGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoLegSecurityAltID(FIXMessageBase):
    """
    NoLegSecurityAltID group fields
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
    
    legSecurityAltID: Optional[str] = Field(None, description='', alias='605')
    legSecurityAltIDSource: Optional[str] = Field(None, description='', alias='606')


class LegSecAltIDGrp(FIXMessageBase):
    """
    FIX 4.4 LegSecAltIDGrp Component
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
    
    noLegSecurityAltID: Optional[int] = Field(None, description='Number of NoLegSecurityAltID entries', alias='604')
    noLegSecurityAltID_items: List[NoLegSecurityAltID] = Field(default_factory=list)
