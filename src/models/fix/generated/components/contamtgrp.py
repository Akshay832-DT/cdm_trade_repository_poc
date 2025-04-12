"""
FIX 4.4 ContAmtGrp Component

This module contains the Pydantic model for the ContAmtGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class ContAmtGrp(TradeModel):
    """
    FIX 4.4 ContAmtGrp Component
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
    ContAmtType: Optional[int] = Field(None, description='', alias='519')
    ContAmtValue: Optional[float] = Field(None, description='', alias='520')
    ContAmtCurr: Optional[str] = Field(None, description='', alias='521')


class NoContAmts(TradeModel):
    """
    NoContAmts group fields
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
    ContAmtType: Optional[int] = Field(None, description='', alias='519')
    ContAmtValue: Optional[float] = Field(None, description='', alias='520')
    ContAmtCurr: Optional[str] = Field(None, description='', alias='521')

    NoContAmtss: List[NoContAmts] = Field(default_factory=list)
