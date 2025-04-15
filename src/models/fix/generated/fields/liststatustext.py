"""
FIX ListStatusText field (tag 444).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ListStatusTextField(FIXFieldBase):
    """"""
    tag: str = "444"
    name: str = "ListStatusText"
    type: str = "STRING"
    value: str
