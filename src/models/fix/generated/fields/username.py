"""
FIX Username field (tag 553).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UsernameField(FIXFieldBase):
    """"""
    tag: str = "553"
    name: str = "Username"
    type: str = "STRING"
    value: str
