"""
FIX Component Model - UndInstrmtGrp
"""

from ..base import FIXComponentBase
from .underlyinginstrument import UnderlyingInstrumentComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoUnderlyingsGroup(FIXComponentBase):

    """FIX Group - NoUnderlyings"""

    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')



class UndInstrmtGrpComponent(FIXComponentBase):
    """FIX Component - UndInstrmtGrp"""


