"""
FIX InvestorCountryOfResidence field (tag 475).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class InvestorCountryOfResidenceField(FIXFieldBase):
    """"""
    tag: str = "475"
    name: str = "InvestorCountryOfResidence"
    type: str = "COUNTRY"
    value: str
