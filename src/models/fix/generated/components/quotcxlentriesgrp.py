"""
FIX Component Model - QuotCxlEntriesGrp
"""

from ..base import FIXComponentBase
from .financingdetails import FinancingDetailsComponent
from .instrmtleggrp import InstrmtLegGrpComponent
from .instrument import InstrumentComponent
from .undinstrmtgrp import UndInstrmtGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoQuoteEntriesGroup(FIXComponentBase):

    """FIX Group - NoQuoteEntries"""

    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')



class QuotCxlEntriesGrpComponent(FIXComponentBase):
    """FIX Component - QuotCxlEntriesGrp"""


