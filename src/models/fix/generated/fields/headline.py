"""
FIX Headline field (tag 148).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class HeadlineField(FIXFieldBase):
    """"""
    tag: str = "148"
    name: str = "Headline"
    type: str = "STRING"
    value: str
