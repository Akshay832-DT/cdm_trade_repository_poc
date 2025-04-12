"""
FIX 4.4 LinesOfTextGrp Component

This module contains the Pydantic model for the LinesOfTextGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class LinesOfTextGrp(FIXMessageBase):
    """
    FIX 4.4 LinesOfTextGrp Component
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
    text: str = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')


class NoLinesOfText(FIXMessageBase):
    """
    NoLinesOfText group fields
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
    text: int = Field(None, description='', alias='33')
    encodedTextLen: Optional[int] = Field(None, description='', alias='33')
    encodedText: Optional[int] = Field(None, description='', alias='33')

    noLinesOfTexts: List[NoLinesOfText] = Field(default_factory=list)
