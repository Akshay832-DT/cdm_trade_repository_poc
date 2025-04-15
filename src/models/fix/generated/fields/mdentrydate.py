"""
FIX MDEntryDate field (tag 272).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MDEntryDateField(FIXFieldBase):
    """"""
    tag: str = "272"
    name: str = "MDEntryDate"
    type: str = "UTCDATEONLY"
    value: date
