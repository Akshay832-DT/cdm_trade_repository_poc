"""
FIX 4.4 QuotCxlEntriesGrp Component

This module contains the Pydantic model for the QuotCxlEntriesGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class QuotCxlEntriesGrp(TradeModel):
    """
    FIX 4.4 QuotCxlEntriesGrp Component
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
    Instrument: Optional[str] = Field(None)
    FinancingDetails: Optional[str] = Field(None)
    UndInstrmtGrp: Optional[str] = Field(None)
    InstrmtLegGrp: Optional[str] = Field(None)


class NoQuoteEntries(TradeModel):
    """
    NoQuoteEntries group fields
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

    NoQuoteEntriess: List[NoQuoteEntries] = Field(default_factory=list)
