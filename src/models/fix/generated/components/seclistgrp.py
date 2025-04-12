"""
FIX 4.4 SecListGrp Component

This module contains the Pydantic model for the SecListGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class SecListGrp(TradeModel):
    """
    FIX 4.4 SecListGrp Component
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
    Currency: Optional[str] = Field(None, description='', alias='15')
    RoundLot: Optional[float] = Field(None, description='', alias='561')
    MinTradeVol: Optional[float] = Field(None, description='', alias='562')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    ExpirationCycle: Optional[int] = Field(None, description='', alias='827')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Instrument: Optional[str] = Field(None)
    InstrumentExtension: Optional[str] = Field(None)
    FinancingDetails: Optional[str] = Field(None)
    UndInstrmtGrp: Optional[str] = Field(None)
    Stipulations: Optional[str] = Field(None)
    InstrmtLegSecListGrp: Optional[str] = Field(None)
    SpreadOrBenchmarkCurveData: Optional[str] = Field(None)
    YieldData: Optional[str] = Field(None)


class NoRelatedSym(TradeModel):
    """
    NoRelatedSym group fields
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
    Currency: Optional[str] = Field(None, description='', alias='15')
    RoundLot: Optional[float] = Field(None, description='', alias='561')
    MinTradeVol: Optional[float] = Field(None, description='', alias='562')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    ExpirationCycle: Optional[int] = Field(None, description='', alias='827')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')

    NoRelatedSyms: List[NoRelatedSym] = Field(default_factory=list)
