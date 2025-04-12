"""
FIX 4.4 AffectedOrdGrp Component

This module contains the Pydantic model for the AffectedOrdGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class AffectedOrdGrp(TradeModel):
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
    OrigClOrdID: Optional[str] = Field(None, description='', alias='41')
    AffectedOrderID: Optional[str] = Field(None, description='', alias='535')
    AffectedSecondaryOrderID: Optional[str] = Field(None, description='', alias='536')


class NoAffectedOrders(TradeModel):
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

    NoAffectedOrderss: List[NoAffectedOrders] = Field(default_factory=list)
