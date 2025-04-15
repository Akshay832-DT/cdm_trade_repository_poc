"""
FIX Component Model - UndInstrmtCollGrp
"""

from ..base import FIXComponentBase
from .underlyinginstrument import UnderlyingInstrumentComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoUnderlyingsGroup(FIXComponentBase):

    """FIX Group - NoUnderlyings"""

    CollAction: Optional[int] = Field(None, alias='944', description='')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')



class UndInstrmtCollGrpComponent(FIXComponentBase):
    """FIX Component - UndInstrmtCollGrp"""


