"""
FIX 4.4 UndInstrmtStrkPxGrp Component

This module contains the Pydantic model for the UndInstrmtStrkPxGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class UndInstrmtStrkPxGrp(TradeModel):
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
    PrevClosePx: Optional[float] = Field(None, description='', alias='140')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    Side: Optional[str] = Field(None, description='', alias='54')
    Price: float = Field(None, description='', alias='44')
    Currency: Optional[str] = Field(None, description='', alias='15')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    UnderlyingInstrument: Optional[str] = Field(None)


class NoUnderlyings(TradeModel):
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
    PrevClosePx: Optional[float] = Field(None, description='', alias='140')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    Side: Optional[str] = Field(None, description='', alias='54')
    Price: float = Field(None, description='', alias='44')
    Currency: Optional[str] = Field(None, description='', alias='15')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')

    NoUnderlyingss: List[NoUnderlyings] = Field(default_factory=list)
