"""
FIX 4.4 ContAmtGrp Component

This module contains the Pydantic model for the ContAmtGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class ContAmtGrp(FIXMessageBase):
    """
    FIX 4.4 ContAmtGrp Component
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
    contAmtType: Optional[int] = Field(None, description='', alias='519')
    contAmtValue: Optional[float] = Field(None, description='', alias='520')
    contAmtCurr: Optional[str] = Field(None, description='', alias='521')


class NoContAmts(FIXMessageBase):
    """
    NoContAmts group fields
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
    contAmtType: Optional[int] = Field(None, description='', alias='518')
    contAmtValue: Optional[int] = Field(None, description='', alias='518')
    contAmtCurr: Optional[int] = Field(None, description='', alias='518')

    noContAmtss: List[NoContAmts] = Field(default_factory=list)
