"""
FIX 4.4 QuotQualGrp Component

This module contains the Pydantic model for the QuotQualGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoQuoteQualifiers(FIXMessageBase):
    """
    NoQuoteQualifiers group fields
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
    
    quoteQualifier: Optional[str] = Field(None, description='', alias='695')


class QuotQualGrp(FIXMessageBase):
    """
    FIX 4.4 QuotQualGrp Component
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
    
    noQuoteQualifiers: Optional[int] = Field(None, description='Number of NoQuoteQualifiers entries', alias='735')
    noQuoteQualifiers_items: List[NoQuoteQualifiers] = Field(default_factory=list)
