"""
FIX HopCompID field (tag 628).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class HopCompIDField(FIXFieldBase):
    """"""
    tag: str = "628"
    name: str = "HopCompID"
    type: str = "STRING"
    value: str
