"""
FIX 4.4 TrdRegTimestamps Component

This module contains the Pydantic model for the TrdRegTimestamps component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoTrdRegTimestampsGroup(FIXComponentBase):
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
    
    TrdRegTimestamp: Optional[datetime] = Field(None, description='', alias='769')
    TrdRegTimestampType: Optional[int] = Field(None, description='', alias='770')
    TrdRegTimestampOrigin: Optional[str] = Field(None, description='', alias='771')


class TrdRegTimestampsComponent(FIXComponentBase):
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
    
    NoTrdRegTimestamps: Optional[int] = Field(None, description='Number of NoTrdRegTimestamps entries', alias='')
    NoTrdRegTimestamps_items: List[NoTrdRegTimestampsGroup] = Field(default_factory=list)
