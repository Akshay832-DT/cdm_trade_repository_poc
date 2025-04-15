"""
FIX ExchangeRule field (tag 825).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExchangeRuleField(FIXFieldBase):
    """"""
    tag: str = "825"
    name: str = "ExchangeRule"
    type: str = "STRING"
    value: str
