"""
FIX Component Model - PosUndInstrmtGrp
"""

from ..base import FIXComponentBase
from .underlyinginstrument import UnderlyingInstrumentComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoUnderlyingsGroup(FIXComponentBase):

    """FIX Group - NoUnderlyings"""

    UnderlyingSettlPrice: float = Field(alias='732', description='')
    UnderlyingSettlPriceType: int = Field(alias='733', description='')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')



class PosUndInstrmtGrpComponent(FIXComponentBase):
    """FIX Component - PosUndInstrmtGrp"""


