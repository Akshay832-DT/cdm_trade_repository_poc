"""
FIX 4.4 TrdCapDtGrp Component

This module contains the Pydantic model for the TrdCapDtGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoDatesGroup(FIXComponentBase):
    """
    NoDates group fields
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
    
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')


class TrdCapDtGrpComponent(FIXComponentBase):
    """
    FIX 4.4 TrdCapDtGrp Component
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
    
    NoDates: Optional[int] = Field(None, description='Number of NoDates entries', alias='')
    NoDates_items: List[NoDatesGroup] = Field(default_factory=list)
