"""
FIX Component Model - QuotSetGrp
"""

from ..base import FIXComponentBase
from .quotentrygrp import QuotEntryGrpComponent
from .underlyinginstrument import UnderlyingInstrumentComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoQuoteSetsGroup(FIXComponentBase):

    """FIX Group - NoQuoteSets"""

    QuoteSetID: str = Field(alias='302', description='')
    QuoteSetValidUntilTime: Optional[datetime] = Field(None, alias='367', description='')
    TotNoQuoteEntries: int = Field(alias='304', description='')
    LastFragment: Optional[bool] = Field(None, alias='893', description='')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')
    QuotEntryGrp: QuotEntryGrpComponent



class QuotSetGrpComponent(FIXComponentBase):
    """FIX Component - QuotSetGrp"""


