"""
FIX RawData field (tag 96).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RawDataField(FIXFieldBase):
    """"""
    tag: str = "96"
    name: str = "RawData"
    type: str = "DATA"
    value: str
