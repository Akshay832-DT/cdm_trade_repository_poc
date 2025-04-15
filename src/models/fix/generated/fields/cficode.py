"""
FIX CFICode field (tag 461).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CFICodeField(FIXFieldBase):
    """"""
    tag: str = "461"
    name: str = "CFICode"
    type: str = "STRING"
    value: str
