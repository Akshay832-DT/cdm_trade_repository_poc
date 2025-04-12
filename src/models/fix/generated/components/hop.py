"""
FIX 4.4 Hop Component

This module contains the Pydantic model for the Hop component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class Hop(FIXMessageBase):
    """
    FIX 4.4 Hop Component
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
    hopCompID: Optional[str] = Field(None, description='', alias='628')
    hopSendingTime: Optional[datetime] = Field(None, description='', alias='629')
    hopRefID: Optional[int] = Field(None, description='', alias='630')


class NoHops(FIXMessageBase):
    """
    NoHops group fields
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
    hopCompID: Optional[int] = Field(None, description='', alias='627')
    hopSendingTime: Optional[int] = Field(None, description='', alias='627')
    hopRefID: Optional[int] = Field(None, description='', alias='627')

    noHopss: List[NoHops] = Field(default_factory=list)
