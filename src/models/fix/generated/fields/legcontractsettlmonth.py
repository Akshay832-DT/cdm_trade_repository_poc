"""
FIX LegContractSettlMonth field (tag 955).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegContractSettlMonthField(FIXFieldBase):
    """"""
    tag: str = "955"
    name: str = "LegContractSettlMonth"
    type: str = "MONTHYEAR"
    value: str
