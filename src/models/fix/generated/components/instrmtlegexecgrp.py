"""
FIX 4.4 InstrmtLegExecGrp Component

This module contains the Pydantic model for the InstrmtLegExecGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class InstrmtLegExecGrp(FIXMessageBase):
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
    legQty: Optional[float] = Field(None, description='', alias='687')
    legSwapType: Optional[int] = Field(None, description='', alias='690')
    legPositionEffect: Optional[str] = Field(None, description='', alias='564')
    legCoveredOrUncovered: Optional[int] = Field(None, description='', alias='565')
    legRefID: Optional[str] = Field(None, description='', alias='654')
    legPrice: Optional[float] = Field(None, description='', alias='566')
    legSettlType: Optional[str] = Field(None, description='', alias='587')
    legSettlDate: Optional[date] = Field(None, description='', alias='588')
    legLastPx: Optional[float] = Field(None, description='', alias='637')
    instrumentLeg: Optional[str] = Field(None)
    legStipulations: Optional[str] = Field(None)
    nestedParties: Optional[str] = Field(None)


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
    legPositionEffect: Optional[int] = Field(None, description='', alias='555')
    legCoveredOrUncovered: Optional[int] = Field(None, description='', alias='555')
    legRefID: Optional[int] = Field(None, description='', alias='555')
    legPrice: Optional[int] = Field(None, description='', alias='555')
    legSettlType: Optional[int] = Field(None, description='', alias='555')
    legSettlDate: Optional[int] = Field(None, description='', alias='555')
    legLastPx: Optional[int] = Field(None, description='', alias='555')

    noLegss: List[NoLegs] = Field(default_factory=list)
