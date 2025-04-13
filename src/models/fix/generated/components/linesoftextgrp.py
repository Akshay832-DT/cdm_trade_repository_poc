"""
FIX 4.4 LinesOfTextGrp Component

This module contains the Pydantic model for the LinesOfTextGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoLinesOfTextGroup(FIXComponentBase):
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
    
    Text: str = Field(..., description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')


class LinesOfTextGrpComponent(FIXComponentBase):
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
    
    NoLinesOfText: Optional[int] = Field(None, description='Number of NoLinesOfText entries', alias='')
    NoLinesOfText_items: List[NoLinesOfTextGroup] = Field(default_factory=list)
