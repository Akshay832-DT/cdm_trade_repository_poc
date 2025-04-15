"""
FIX Component Model - InstrmtMDReqGrp
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

    Instrument: InstrumentComponent
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')



class InstrmtMDReqGrpComponent(FIXComponentBase):
    """FIX Component - InstrmtMDReqGrp"""


