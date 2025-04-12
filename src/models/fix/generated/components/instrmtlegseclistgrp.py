"""
FIX 4.4 InstrmtLegSecListGrp Component

This module contains the Pydantic model for the InstrmtLegSecListGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class InstrmtLegSecListGrp(TradeModel):
    """
    FIX 4.4 InstrmtLegSecListGrp Component
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
    LegSwapType: Optional[int] = Field(None, description='', alias='690')
    LegSettlType: Optional[str] = Field(None, description='', alias='587')
    InstrumentLeg: Optional[str] = Field(None)
    LegStipulations: Optional[str] = Field(None)
    LegBenchmarkCurveData: Optional[str] = Field(None)


class NoLegs(TradeModel):
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
    LegSwapType: Optional[int] = Field(None, description='', alias='690')
    LegSettlType: Optional[str] = Field(None, description='', alias='587')

    NoLegss: List[NoLegs] = Field(default_factory=list)
