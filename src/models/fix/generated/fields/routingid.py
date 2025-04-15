"""
FIX RoutingID field (tag 217).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RoutingIDField(FIXFieldBase):
    """"""
    tag: str = "217"
    name: str = "RoutingID"
    type: str = "STRING"
    value: str
