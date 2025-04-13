"""
FIX 4.4 ContraGrp Component

This module contains the Pydantic model for the ContraGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class NoContraBrokers(FIXMessageBase):
    """
    NoContraBrokers group fields
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
    
    contraBroker: Optional[str] = Field(None, description='', alias='375')
    contraTrader: Optional[str] = Field(None, description='', alias='337')
    contraTradeQty: Optional[float] = Field(None, description='', alias='437')
    contraTradeTime: Optional[datetime] = Field(None, description='', alias='438')
    contraLegRefID: Optional[str] = Field(None, description='', alias='655')


class ContraGrp(FIXMessageBase):
    """
    FIX 4.4 ContraGrp Component
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
    
    noContraBrokers: Optional[int] = Field(None, description='Number of NoContraBrokers entries', alias='382')
    noContraBrokers_items: List[NoContraBrokers] = Field(default_factory=list)
