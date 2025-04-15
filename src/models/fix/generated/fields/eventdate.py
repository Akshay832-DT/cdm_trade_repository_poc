"""
FIX EventDate field (tag 866).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EventDateField(FIXFieldBase):
    """"""
    tag: str = "866"
    name: str = "EventDate"
    type: str = "LOCALMKTDATE"
    value: date
