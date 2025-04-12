"""
FIX 4.4 CollInqQualGrp Component

This module contains the Pydantic model for the CollInqQualGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class CollInqQualGrp(FIXMessageBase):
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
    collInquiryQualifier: Optional[int] = Field(None, description='', alias='896')


class NoCollInquiryQualifier(FIXMessageBase):
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
    collInquiryQualifier: Optional[int] = Field(None, description='', alias='938')

    noCollInquiryQualifiers: List[NoCollInquiryQualifier] = Field(default_factory=list)
