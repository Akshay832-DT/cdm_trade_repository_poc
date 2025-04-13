"""
FIX 4.4 Hop Component

This module contains the Pydantic model for the Hop component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoHopsGroup(FIXComponentBase):
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
    
    HopCompID: Optional[str] = Field(None, description='', alias='628')
    HopSendingTime: Optional[datetime] = Field(None, description='', alias='629')
    HopRefID: Optional[int] = Field(None, description='', alias='630')


class HopComponent(FIXComponentBase):
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
    
    NoHops: Optional[int] = Field(None, description='Number of NoHops entries', alias='')
    NoHops_items: List[NoHopsGroup] = Field(default_factory=list)
