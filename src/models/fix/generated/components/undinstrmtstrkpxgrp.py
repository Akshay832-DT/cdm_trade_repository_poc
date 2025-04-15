"""
FIX Component Model - UndInstrmtStrkPxGrp
"""

from ..base import FIXComponentBase
from .underlyinginstrument import UnderlyingInstrumentComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoUnderlyingsGroup(FIXComponentBase):

    """FIX Group - NoUnderlyings"""

    PrevClosePx: Optional[float] = Field(None, alias='140', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    Price: float = Field(alias='44', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')



class UndInstrmtStrkPxGrpComponent(FIXComponentBase):
    """FIX Component - UndInstrmtStrkPxGrp"""


