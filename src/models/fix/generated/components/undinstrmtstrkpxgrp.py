"""
FIX 4.4 UndInstrmtStrkPxGrp Component

This module contains the Pydantic model for the UndInstrmtStrkPxGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


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
    prevClosePx: Optional[float] = Field(None, description='', alias='140')
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    side: Optional[str] = Field(None, description='', alias='54')
    price: float = Field(None, description='', alias='44')
    currency: Optional[str] = Field(None, description='', alias='15')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    underlyingInstrument: Optional[str] = Field(None)


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
    prevClosePx: Optional[int] = Field(None, description='', alias='711')
    clOrdID: Optional[int] = Field(None, description='', alias='711')
    secondaryClOrdID: Optional[int] = Field(None, description='', alias='711')
    side: Optional[int] = Field(None, description='', alias='711')
    price: int = Field(None, description='', alias='711')
    currency: Optional[int] = Field(None, description='', alias='711')
    text: Optional[int] = Field(None, description='', alias='711')
    encodedTextLen: Optional[int] = Field(None, description='', alias='711')
    encodedText: Optional[int] = Field(None, description='', alias='711')

    noUnderlyingss: List[NoUnderlyings] = Field(default_factory=list)
