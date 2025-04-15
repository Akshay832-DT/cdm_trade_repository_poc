"""
FIX DeliverToLocationID field (tag 145).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DeliverToLocationIDField(FIXFieldBase):
    """"""
    tag: str = "145"
    name: str = "DeliverToLocationID"
    type: str = "STRING"
    value: str
