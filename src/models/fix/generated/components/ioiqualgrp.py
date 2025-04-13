"""
FIX 4.4 IOIQualGrp Component

This module contains the Pydantic model for the IOIQualGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoIOIQualifiers(FIXMessageBase):
    """
    NoIOIQualifiers group fields
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
    
    iOIQualifier: Optional[str] = Field(None, description='', alias='104')


class IOIQualGrp(FIXMessageBase):
    """
    FIX 4.4 IOIQualGrp Component
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
    
    noIOIQualifiers: Optional[int] = Field(None, description='Number of NoIOIQualifiers entries', alias='199')
    noIOIQualifiers_items: List[NoIOIQualifiers] = Field(default_factory=list)
