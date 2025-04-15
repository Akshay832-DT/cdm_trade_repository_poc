"""
FIX PartySubID field (tag 523).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PartySubIDField(FIXFieldBase):
    """"""
    tag: str = "523"
    name: str = "PartySubID"
    type: str = "STRING"
    value: str
