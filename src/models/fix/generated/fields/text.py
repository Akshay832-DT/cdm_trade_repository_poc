"""
FIX Text field (tag 58).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TextField(FIXFieldBase):
    """"""
    tag: str = "58"
    name: str = "Text"
    type: str = "STRING"
    value: str
