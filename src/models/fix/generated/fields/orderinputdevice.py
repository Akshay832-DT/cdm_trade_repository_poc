"""
FIX OrderInputDevice field (tag 821).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class OrderInputDeviceField(FIXFieldBase):
    """"""
    tag: str = "821"
    name: str = "OrderInputDevice"
    type: str = "STRING"
    value: str
