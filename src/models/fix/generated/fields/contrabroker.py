"""
FIX ContraBroker field (tag 375).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ContraBrokerField(FIXFieldBase):
    """"""
    tag: str = "375"
    name: str = "ContraBroker"
    type: str = "STRING"
    value: str
