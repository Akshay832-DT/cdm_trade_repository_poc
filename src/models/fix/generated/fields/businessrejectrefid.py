"""
FIX BusinessRejectRefID field (tag 379).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BusinessRejectRefIDField(FIXFieldBase):
    """"""
    tag: str = "379"
    name: str = "BusinessRejectRefID"
    type: str = "STRING"
    value: str
