"""
FIX 4.4 RFQReqGrp Component

This module contains the Pydantic model for the RFQReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoRelatedSymGroup(FIXComponentBase):
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
    
    PrevClosePx: Optional[float] = Field(None, description='', alias='140')
    QuoteRequestType: Optional[int] = Field(None, description='', alias='303')
    QuoteType: Optional[int] = Field(None, description='', alias='537')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')


class RFQReqGrpComponent(FIXComponentBase):
    """
    FIX 4.4 RFQReqGrp Component
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
    
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    NoRelatedSym: Optional[int] = Field(None, description='Number of NoRelatedSym entries', alias='')
    NoRelatedSym_items: List[NoRelatedSymGroup] = Field(default_factory=list)
