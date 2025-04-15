"""
FIX Account field (tag 1).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AccountField(FIXFieldBase):
    """"""
    tag: str = "1"
    name: str = "Account"
    type: str = "STRING"
    value: str
