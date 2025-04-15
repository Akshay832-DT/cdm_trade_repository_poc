"""
FIX DeliverToSubID field (tag 129).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DeliverToSubIDField(FIXFieldBase):
    """"""
    tag: str = "129"
    name: str = "DeliverToSubID"
    type: str = "STRING"
    value: str
