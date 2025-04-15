"""
FIX LocationID field (tag 283).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LocationIDField(FIXFieldBase):
    """"""
    tag: str = "283"
    name: str = "LocationID"
    type: str = "STRING"
    value: str
