"""
FIX 4.4 InstrmtLegExecGrp Component

This module contains the Pydantic model for the InstrmtLegExecGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class InstrmtLegExecGrp(TradeModel):
    """
    FIX 4.4 InstrmtLegExecGrp Component
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
    InstrumentLeg: Optional[str] = Field(None)
    LegStipulations: Optional[str] = Field(None)
    NestedParties: Optional[str] = Field(None)


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
    LegPositionEffect: Optional[str] = Field(None, description='', alias='564')
    LegCoveredOrUncovered: Optional[int] = Field(None, description='', alias='565')
    LegRefID: Optional[str] = Field(None, description='', alias='654')
    LegPrice: Optional[float] = Field(None, description='', alias='566')
    LegSettlType: Optional[str] = Field(None, description='', alias='587')
    LegSettlDate: Optional[date] = Field(None, description='', alias='588')
    LegLastPx: Optional[float] = Field(None, description='', alias='637')

    NoLegss: List[NoLegs] = Field(default_factory=list)
