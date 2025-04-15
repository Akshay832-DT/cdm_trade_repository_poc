"""
FIX IOIRefID field (tag 26).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class IOIRefIDField(FIXFieldBase):
    """"""
    tag: str = "26"
    name: str = "IOIRefID"
    type: str = "STRING"
    value: str
