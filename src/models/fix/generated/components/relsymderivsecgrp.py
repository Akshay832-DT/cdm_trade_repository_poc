"""
FIX Component Model - RelSymDerivSecGrp
"""

from ..base import FIXComponentBase
from .instrmtleggrp import InstrmtLegGrpComponent
from .instrument import InstrumentComponent
from .instrumentextension import InstrumentExtensionComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoRelatedSymGroup(FIXComponentBase):

    """FIX Group - NoRelatedSym"""

    Currency: Optional[str] = Field(None, alias='15', description='')
    ExpirationCycle: Optional[int] = Field(None, alias='827', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')



class RelSymDerivSecGrpComponent(FIXComponentBase):
    """FIX Component - RelSymDerivSecGrp"""


