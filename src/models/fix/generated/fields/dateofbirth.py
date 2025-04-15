"""
FIX DateOfBirth field (tag 486).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DateOfBirthField(FIXFieldBase):
    """"""
    tag: str = "486"
    name: str = "DateOfBirth"
    type: str = "LOCALMKTDATE"
    value: date
