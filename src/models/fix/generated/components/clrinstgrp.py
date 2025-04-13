"""
FIX 4.4 ClrInstGrp Component

This module contains the Pydantic model for the ClrInstGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoClearingInstructionsGroup(FIXComponentBase):
    """
    NoClearingInstructions group fields
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
    
    ClearingInstruction: Optional[int] = Field(None, description='', alias='577')


class ClrInstGrpComponent(FIXComponentBase):
    """
    FIX 4.4 ClrInstGrp Component
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
    
    NoClearingInstructions: Optional[int] = Field(None, description='Number of NoClearingInstructions entries', alias='')
    NoClearingInstructions_items: List[NoClearingInstructionsGroup] = Field(default_factory=list)
