"""
FIX SecurityExchange field (tag 207).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityExchangeField(FIXFieldBase):
    """"""
    tag: str = "207"
    name: str = "SecurityExchange"
    type: str = "EXCHANGE"
    value: str
