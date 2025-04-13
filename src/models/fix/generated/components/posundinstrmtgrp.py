"""
FIX 4.4 PosUndInstrmtGrp Component

This module contains the Pydantic model for the PosUndInstrmtGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoUnderlyingsGroup(FIXComponentBase):
    """
    NoUnderlyings group fields
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
    
    UnderlyingSettlPrice: float = Field(..., description='', alias='732')
    UnderlyingSettlPriceType: int = Field(..., description='', alias='733')


class PosUndInstrmtGrpComponent(FIXComponentBase):
    """
    FIX 4.4 PosUndInstrmtGrp Component
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
    
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='UnderlyingInstrument component')
    NoUnderlyings: Optional[int] = Field(None, description='Number of NoUnderlyings entries', alias='')
    NoUnderlyings_items: List[NoUnderlyingsGroup] = Field(default_factory=list)
