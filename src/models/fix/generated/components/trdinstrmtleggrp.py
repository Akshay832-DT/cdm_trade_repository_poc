"""
FIX 4.4 TrdInstrmtLegGrp Component

This module contains the Pydantic model for the TrdInstrmtLegGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoLegsGroup(FIXComponentBase):
    """
    NoLegs group fields
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
    
    LegQty: Optional[float] = Field(None, description='', alias='687')
    LegSwapType: Optional[int] = Field(None, description='', alias='690')
    LegPositionEffect: Optional[str] = Field(None, description='', alias='564')
    LegCoveredOrUncovered: Optional[int] = Field(None, description='', alias='565')
    LegRefID: Optional[str] = Field(None, description='', alias='654')
    LegPrice: Optional[float] = Field(None, description='', alias='566')
    LegSettlType: Optional[str] = Field(None, description='', alias='587')
    LegSettlDate: Optional[date] = Field(None, description='', alias='588')
    LegLastPx: Optional[float] = Field(None, description='', alias='637')


class TrdInstrmtLegGrpComponent(FIXComponentBase):
    """
    FIX 4.4 TrdInstrmtLegGrp Component
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
    
    InstrumentLeg: Optional[InstrumentLegComponent] = Field(None, description='InstrumentLeg component')
    LegStipulations: Optional[LegStipulationsComponent] = Field(None, description='LegStipulations component')
    NestedParties: Optional[NestedPartiesComponent] = Field(None, description='NestedParties component')
    NoLegs: Optional[int] = Field(None, description='Number of NoLegs entries', alias='')
    NoLegs_items: List[NoLegsGroup] = Field(default_factory=list)
