"""
FIX XmlDataLen field (tag 212).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class XmlDataLenField(FIXFieldBase):
    """"""
    tag: str = "212"
    name: str = "XmlDataLen"
    type: str = "LENGTH"
    value: int
