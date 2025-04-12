"""
FIX 4.4 CollInqQualGrp Component

This module contains the Pydantic model for the CollInqQualGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class CollInqQualGrp(TradeModel):
    """
    FIX 4.4 CollInqQualGrp Component
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
    CollInquiryQualifier: Optional[int] = Field(None, description='', alias='896')


class NoCollInquiryQualifier(TradeModel):
    """
    NoCollInquiryQualifier group fields
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
    CollInquiryQualifier: Optional[int] = Field(None, description='', alias='896')

    NoCollInquiryQualifiers: List[NoCollInquiryQualifier] = Field(default_factory=list)
