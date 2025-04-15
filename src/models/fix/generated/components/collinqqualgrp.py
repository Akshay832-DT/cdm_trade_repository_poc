"""
FIX Component Model - CollInqQualGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoCollInquiryQualifierGroup(FIXComponentBase):

    """FIX Group - NoCollInquiryQualifier"""

    CollInquiryQualifier: Optional[int] = Field(None, alias='896', description='')



class CollInqQualGrpComponent(FIXComponentBase):
    """FIX Component - CollInqQualGrp"""


