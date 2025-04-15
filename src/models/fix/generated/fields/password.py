"""
FIX Password field (tag 554).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PasswordField(FIXFieldBase):
    """"""
    tag: str = "554"
    name: str = "Password"
    type: str = "STRING"
    value: str
