"""
FIX Component Model - RFQReqGrp
"""

from ..base import FIXComponentBase
from .instrmtleggrp import InstrmtLegGrpComponent
from .instrument import InstrumentComponent
from .undinstrmtgrp import UndInstrmtGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoRelatedSymGroup(FIXComponentBase):

    """FIX Group - NoRelatedSym"""

    PrevClosePx: Optional[float] = Field(None, alias='140', description='')
    QuoteRequestType: Optional[int] = Field(None, alias='303', description='')
    QuoteType: Optional[int] = Field(None, alias='537', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Instrument: InstrumentComponent
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')



class RFQReqGrpComponent(FIXComponentBase):
    """FIX Component - RFQReqGrp"""


