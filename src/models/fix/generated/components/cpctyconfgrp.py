"""
FIX 4.4 CpctyConfGrp Component

This module contains the Pydantic model for the CpctyConfGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoCapacitiesGroup(FIXComponentBase):
    """
    NoCapacities group fields
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
    
    OrderCapacity: str = Field(..., description='', alias='528')
    OrderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    OrderCapacityQty: float = Field(..., description='', alias='863')


class CpctyConfGrpComponent(FIXComponentBase):
    """
    FIX 4.4 CpctyConfGrp Component
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
    
    NoCapacities: Optional[int] = Field(None, description='Number of NoCapacities entries', alias='')
    NoCapacities_items: List[NoCapacitiesGroup] = Field(default_factory=list)
