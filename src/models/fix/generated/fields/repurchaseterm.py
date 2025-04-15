"""
FIX RepurchaseTerm field (tag 226).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RepurchaseTermField(FIXFieldBase):
    """"""
    tag: str = "226"
    name: str = "RepurchaseTerm"
    type: str = "INT"
    value: int
