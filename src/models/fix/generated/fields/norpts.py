"""
FIX NoRpts field (tag 82).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoRptsField(FIXFieldBase):
    """"""
    tag: str = "82"
    name: str = "NoRpts"
    type: str = "INT"
    value: int
