"""
FIX EncodedListStatusText field (tag 446).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedListStatusTextField(FIXFieldBase):
    """"""
    tag: str = "446"
    name: str = "EncodedListStatusText"
    type: str = "DATA"
    value: str
