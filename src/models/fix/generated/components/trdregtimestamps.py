"""
FIX 4.4 TrdRegTimestamps Component

This module contains the Pydantic model for the TrdRegTimestamps component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class TrdRegTimestamps(FIXMessageBase):
    """
    FIX 4.4 TrdRegTimestamps Component
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
    trdRegTimestamp: Optional[datetime] = Field(None, description='', alias='769')
    trdRegTimestampType: Optional[int] = Field(None, description='', alias='770')
    trdRegTimestampOrigin: Optional[str] = Field(None, description='', alias='771')


class NoTrdRegTimestamps(FIXMessageBase):
    """
    NoTrdRegTimestamps group fields
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
    trdRegTimestamp: Optional[int] = Field(None, description='', alias='768')
    trdRegTimestampType: Optional[int] = Field(None, description='', alias='768')
    trdRegTimestampOrigin: Optional[int] = Field(None, description='', alias='768')

    noTrdRegTimestampss: List[NoTrdRegTimestamps] = Field(default_factory=list)
