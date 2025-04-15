"""
FIX DatedDate field (tag 873).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DatedDateField(FIXFieldBase):
    """"""
    tag: str = "873"
    name: str = "DatedDate"
    type: str = "LOCALMKTDATE"
    value: date
