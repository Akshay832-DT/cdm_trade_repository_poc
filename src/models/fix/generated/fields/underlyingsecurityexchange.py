"""
FIX UnderlyingSecurityExchange field (tag 308).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UnderlyingSecurityExchangeField(FIXFieldBase):
    """"""
    tag: str = "308"
    name: str = "UnderlyingSecurityExchange"
    type: str = "EXCHANGE"
    value: str
