"""
FIX 4.4 SecListGrp Component

This module contains the Pydantic model for the SecListGrp component.
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
    
    Currency: Optional[str] = Field(None, description='', alias='15')
    RoundLot: Optional[float] = Field(None, description='', alias='561')
    MinTradeVol: Optional[float] = Field(None, description='', alias='562')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    ExpirationCycle: Optional[int] = Field(None, description='', alias='827')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')


class SecListGrpComponent(FIXComponentBase):
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
    
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='InstrumentExtension component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='Stipulations component')
    InstrmtLegSecListGrp: Optional[InstrmtLegSecListGrpComponent] = Field(None, description='InstrmtLegSecListGrp component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='SpreadOrBenchmarkCurveData component')
    YieldData: Optional[YieldDataComponent] = Field(None, description='YieldData component')
    NoRelatedSym: Optional[int] = Field(None, description='Number of NoRelatedSym entries', alias='')
    NoRelatedSym_items: List[NoRelatedSymGroup] = Field(default_factory=list)
