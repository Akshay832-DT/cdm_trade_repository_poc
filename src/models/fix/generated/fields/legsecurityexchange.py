"""
FIX LegSecurityExchange field (tag 616).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LegSecurityExchangeField(FIXFieldBase):
    """"""
    tag: str = "616"
    name: str = "LegSecurityExchange"
    type: str = "EXCHANGE"
    value: str
