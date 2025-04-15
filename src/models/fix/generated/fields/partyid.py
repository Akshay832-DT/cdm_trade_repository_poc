"""
FIX PartyID field (tag 448).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PartyIDField(FIXFieldBase):
    """"""
    tag: str = "448"
    name: str = "PartyID"
    type: str = "STRING"
    value: str
