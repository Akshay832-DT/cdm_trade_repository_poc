"""
FIX NetworkRequestID field (tag 933).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NetworkRequestIDField(FIXFieldBase):
    """"""
    tag: str = "933"
    name: str = "NetworkRequestID"
    type: str = "STRING"
    value: str
