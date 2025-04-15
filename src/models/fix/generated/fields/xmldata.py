"""
FIX XmlData field (tag 213).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class XmlDataField(FIXFieldBase):
    """"""
    tag: str = "213"
    name: str = "XmlData"
    type: str = "DATA"
    value: str
