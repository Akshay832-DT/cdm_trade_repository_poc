"""
FIX 4.4 QuotQualGrp Component

This module contains the Pydantic model for the QuotQualGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class QuotQualGrp(TradeModel):
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
    QuoteQualifier: Optional[str] = Field(None, description='', alias='695')


class NoQuoteQualifiers(TradeModel):
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
    QuoteQualifier: Optional[str] = Field(None, description='', alias='695')

    NoQuoteQualifierss: List[NoQuoteQualifiers] = Field(default_factory=list)
