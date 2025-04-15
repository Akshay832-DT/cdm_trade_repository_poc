"""
FIX Component Model - QuotSetAckGrp
"""

from ..base import FIXComponentBase
from .quotentryackgrp import QuotEntryAckGrpComponent
from .underlyinginstrument import UnderlyingInstrumentComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoQuoteSetsGroup(FIXComponentBase):

    """FIX Group - NoQuoteSets"""

    QuoteSetID: Optional[str] = Field(None, alias='302', description='')
    TotNoQuoteEntries: Optional[int] = Field(None, alias='304', description='')
    LastFragment: Optional[bool] = Field(None, alias='893', description='')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')
    QuotEntryAckGrp: Optional[QuotEntryAckGrpComponent] = Field(None, description='')



class QuotSetAckGrpComponent(FIXComponentBase):
    """FIX Component - QuotSetAckGrp"""


