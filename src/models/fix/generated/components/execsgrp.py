"""
FIX 4.4 ExecsGrp Component

This module contains the Pydantic model for the ExecsGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoExecsGroup(FIXComponentBase):
    """
    NoExecs group fields
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
    
    ExecID: Optional[str] = Field(None, description='', alias='17')


class ExecsGrpComponent(FIXComponentBase):
    """
    FIX 4.4 ExecsGrp Component
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
    
    NoExecs: Optional[int] = Field(None, description='Number of NoExecs entries', alias='')
    NoExecs_items: List[NoExecsGroup] = Field(default_factory=list)
