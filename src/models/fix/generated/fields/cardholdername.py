"""
FIX CardHolderName field (tag 488).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CardHolderNameField(FIXFieldBase):
    """"""
    tag: str = "488"
    name: str = "CardHolderName"
    type: str = "STRING"
    value: str
