"""
FIX CardIssNum field (tag 491).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CardIssNumField(FIXFieldBase):
    """"""
    tag: str = "491"
    name: str = "CardIssNum"
    type: str = "STRING"
    value: str
