"""
FIX Component Model - SecListGrp
"""

from ..base import FIXComponentBase
from .financingdetails import FinancingDetailsComponent
from .instrmtlegseclistgrp import InstrmtLegSecListGrpComponent
from .instrument import InstrumentComponent
from .instrumentextension import InstrumentExtensionComponent
from .spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from .stipulations import StipulationsComponent
from .undinstrmtgrp import UndInstrmtGrpComponent
from .yielddata import YieldDataComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoRelatedSymGroup(FIXComponentBase):

    """FIX Group - NoRelatedSym"""

    Currency: Optional[str] = Field(None, alias='15', description='')
    RoundLot: Optional[float] = Field(None, alias='561', description='')
    MinTradeVol: Optional[float] = Field(None, alias='562', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    ExpirationCycle: Optional[int] = Field(None, alias='827', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='')
    InstrmtLegSecListGrp: Optional[InstrmtLegSecListGrpComponent] = Field(None, description='')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='')
    YieldData: Optional[YieldDataComponent] = Field(None, description='')



class SecListGrpComponent(FIXComponentBase):
    """FIX Component - SecListGrp"""


