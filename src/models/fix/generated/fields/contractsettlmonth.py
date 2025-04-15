"""
FIX ContractSettlMonth field (tag 667).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContractSettlMonthField(FIXFieldBase):
    """"""
    tag: str = "667"
    name: str = "ContractSettlMonth"
    type: str = "MONTHYEAR"
    value: str
