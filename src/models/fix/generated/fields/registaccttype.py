"""
FIX RegistAcctType field (tag 493).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RegistAcctTypeField(FIXFieldBase):
    """"""
    tag: str = "493"
    name: str = "RegistAcctType"
    type: str = "STRING"
    value: str
