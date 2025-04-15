"""
FIX BookingRefID field (tag 466).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BookingRefIDField(FIXFieldBase):
    """"""
    tag: str = "466"
    name: str = "BookingRefID"
    type: str = "STRING"
    value: str
