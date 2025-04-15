"""
FIX EventText field (tag 868).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EventTextField(FIXFieldBase):
    """"""
    tag: str = "868"
    name: str = "EventText"
    type: str = "STRING"
    value: str
