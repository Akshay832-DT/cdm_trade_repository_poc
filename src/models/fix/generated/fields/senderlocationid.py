"""
FIX SenderLocationID field (tag 142).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SenderLocationIDField(FIXFieldBase):
    """"""
    tag: str = "142"
    name: str = "SenderLocationID"
    type: str = "STRING"
    value: str
