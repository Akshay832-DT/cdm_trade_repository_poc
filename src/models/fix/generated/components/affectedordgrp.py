"""
FIX 4.4 AffectedOrdGrp Component

This module contains the Pydantic model for the AffectedOrdGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoAffectedOrdersGroup(FIXComponentBase):
    """
    NoAffectedOrders group fields
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
    
    OrigClOrdID: Optional[str] = Field(None, description='', alias='41')
    AffectedOrderID: Optional[str] = Field(None, description='', alias='535')
    AffectedSecondaryOrderID: Optional[str] = Field(None, description='', alias='536')


class AffectedOrdGrpComponent(FIXComponentBase):
    """
    FIX 4.4 AffectedOrdGrp Component
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
    
    NoAffectedOrders: Optional[int] = Field(None, description='Number of NoAffectedOrders entries', alias='')
    NoAffectedOrders_items: List[NoAffectedOrdersGroup] = Field(default_factory=list)
