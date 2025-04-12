"""
FIX 4.4 LegQuotGrp Component

This module contains the Pydantic model for the LegQuotGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class LegQuotGrp(TradeModel):
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
    LegQty: Optional[float] = Field(None, description='', alias='687')
    LegSwapType: Optional[int] = Field(None, description='', alias='690')
    LegSettlType: Optional[str] = Field(None, description='', alias='587')
    LegSettlDate: Optional[date] = Field(None, description='', alias='588')
    LegPriceType: Optional[int] = Field(None, description='', alias='686')
    LegBidPx: Optional[float] = Field(None, description='', alias='681')
    LegOfferPx: Optional[float] = Field(None, description='', alias='684')
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
    LegPriceType: Optional[int] = Field(None, description='', alias='686')
    LegBidPx: Optional[float] = Field(None, description='', alias='681')
    LegOfferPx: Optional[float] = Field(None, description='', alias='684')

    NoLegss: List[NoLegs] = Field(default_factory=list)
