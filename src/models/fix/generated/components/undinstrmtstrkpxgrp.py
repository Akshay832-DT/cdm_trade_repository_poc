"""
FIX 4.4 UndInstrmtStrkPxGrp Component

This module contains the Pydantic model for the UndInstrmtStrkPxGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrument


class NoUnderlyings(FIXMessageBase):
    """
    NoUnderlyings group fields
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
    
    prevClosePx: Optional[float] = Field(None, description='', alias='140')
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    side: Optional[str] = Field(None, description='', alias='54')
    price: float = Field(..., description='', alias='44')
    currency: Optional[str] = Field(None, description='', alias='15')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')


class UndInstrmtStrkPxGrp(FIXMessageBase):
    """
    FIX 4.4 UndInstrmtStrkPxGrp Component
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
    
    underlyingInstrument: Optional[UnderlyingInstrument] = Field(None, description='UnderlyingInstrument component')
    noUnderlyings: Optional[int] = Field(None, description='Number of NoUnderlyings entries', alias='711')
    noUnderlyings_items: List[NoUnderlyings] = Field(default_factory=list)
