"""
FIX 4.4 QuotReqLegsGrp Component

This module contains the Pydantic model for the QuotReqLegsGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class QuotReqLegsGrp(TradeModel):
    """
    FIX 4.4 QuotReqLegsGrp Component
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
    InstrumentLeg: Optional[str] = Field(None)
    LegStipulations: Optional[str] = Field(None)
    NestedParties: Optional[str] = Field(None)
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
    LegQty: Optional[float] = Field(None, description='', alias='687')
    LegSwapType: Optional[int] = Field(None, description='', alias='690')
    LegSettlType: Optional[str] = Field(None, description='', alias='587')
    LegSettlDate: Optional[date] = Field(None, description='', alias='588')

    NoLegss: List[NoLegs] = Field(default_factory=list)
