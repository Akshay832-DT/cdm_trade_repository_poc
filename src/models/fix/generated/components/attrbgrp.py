"""
FIX 4.4 AttrbGrp Component

This module contains the Pydantic model for the AttrbGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoInstrAttribGroup(FIXComponentBase):
    """
    NoInstrAttrib group fields
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
    
    InstrAttribType: Optional[int] = Field(None, description='', alias='871')
    InstrAttribValue: Optional[str] = Field(None, description='', alias='872')


class AttrbGrpComponent(FIXComponentBase):
    """
    FIX 4.4 AttrbGrp Component
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
    
    NoInstrAttrib: Optional[int] = Field(None, description='Number of NoInstrAttrib entries', alias='')
    NoInstrAttrib_items: List[NoInstrAttribGroup] = Field(default_factory=list)
