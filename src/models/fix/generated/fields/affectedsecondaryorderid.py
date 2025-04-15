"""
FIX AffectedSecondaryOrderID field (tag 536).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AffectedSecondaryOrderIDField(FIXFieldBase):
    """"""
    tag: str = "536"
    name: str = "AffectedSecondaryOrderID"
    type: str = "STRING"
    value: str
