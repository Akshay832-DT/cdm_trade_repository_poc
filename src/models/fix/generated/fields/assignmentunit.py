"""
FIX AssignmentUnit field (tag 745).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AssignmentUnitField(FIXFieldBase):
    """"""
    tag: str = "745"
    name: str = "AssignmentUnit"
    type: str = "QTY"
    value: float
