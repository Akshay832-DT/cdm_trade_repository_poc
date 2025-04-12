"""
FIX 4.4 LegQuotGrp Component

This module contains the Pydantic model for the LegQuotGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class LegQuotGrp(FIXMessageBase):
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
    legQty: Optional[float] = Field(None, description='', alias='687')
    legSwapType: Optional[int] = Field(None, description='', alias='690')
    legSettlType: Optional[str] = Field(None, description='', alias='587')
    legSettlDate: Optional[date] = Field(None, description='', alias='588')
    legPriceType: Optional[int] = Field(None, description='', alias='686')
    legBidPx: Optional[float] = Field(None, description='', alias='681')
    legOfferPx: Optional[float] = Field(None, description='', alias='684')
    instrumentLeg: Optional[str] = Field(None)
    legStipulations: Optional[str] = Field(None)
    nestedParties: Optional[str] = Field(None)
    legBenchmarkCurveData: Optional[str] = Field(None)


class NoLegs(FIXMessageBase):
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
    legQty: Optional[int] = Field(None, description='', alias='555')
    legSwapType: Optional[int] = Field(None, description='', alias='555')
    legSettlType: Optional[int] = Field(None, description='', alias='555')
    legSettlDate: Optional[int] = Field(None, description='', alias='555')
    legPriceType: Optional[int] = Field(None, description='', alias='555')
    legBidPx: Optional[int] = Field(None, description='', alias='555')
    legOfferPx: Optional[int] = Field(None, description='', alias='555')

    noLegss: List[NoLegs] = Field(default_factory=list)
