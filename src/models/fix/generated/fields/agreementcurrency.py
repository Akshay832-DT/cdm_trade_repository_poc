"""
FIX AgreementCurrency field (tag 918).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AgreementCurrencyField(FIXFieldBase):
    """"""
    tag: str = "918"
    name: str = "AgreementCurrency"
    type: str = "CURRENCY"
    value: str
