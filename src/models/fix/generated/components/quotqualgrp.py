"""
FIX Component Model - QuotQualGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoQuoteQualifiersGroup(FIXComponentBase):

    """FIX Group - NoQuoteQualifiers"""

    QuoteQualifier: Optional[str] = Field(None, alias='695', description='')



class QuotQualGrpComponent(FIXComponentBase):
    """FIX Component - QuotQualGrp"""


