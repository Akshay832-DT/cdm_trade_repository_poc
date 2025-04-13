"""
FIX 4.4 SecAltIDGrp Component

This module contains the Pydantic model for the SecAltIDGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoSecurityAltIDGroup(FIXComponentBase):
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


class SecAltIDGrpComponent(FIXComponentBase):
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
    
    NoSecurityAltID: Optional[int] = Field(None, description='Number of NoSecurityAltID entries', alias='')
    NoSecurityAltID_items: List[NoSecurityAltIDGroup] = Field(default_factory=list)
