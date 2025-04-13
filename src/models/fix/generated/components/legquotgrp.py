"""
FIX 4.4 LegQuotGrp Component

This module contains the Pydantic model for the LegQuotGrp component.
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
    LegSettlType: Optional[str] = Field(None, description='', alias='587')
    LegSettlDate: Optional[date] = Field(None, description='', alias='588')
    LegPriceType: Optional[int] = Field(None, description='', alias='686')
    LegBidPx: Optional[float] = Field(None, description='', alias='681')
    LegOfferPx: Optional[float] = Field(None, description='', alias='684')


class LegQuotGrpComponent(FIXComponentBase):
    """
    FIX 4.4 LegQuotGrp Component
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
    LegBenchmarkCurveData: Optional[LegBenchmarkCurveDataComponent] = Field(None, description='LegBenchmarkCurveData component')
    NoLegs: Optional[int] = Field(None, description='Number of NoLegs entries', alias='')
    NoLegs_items: List[NoLegsGroup] = Field(default_factory=list)
