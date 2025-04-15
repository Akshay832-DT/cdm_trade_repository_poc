"""
FIX UserStatusText field (tag 927).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UserStatusTextField(FIXFieldBase):
    """"""
    tag: str = "927"
    name: str = "UserStatusText"
    type: str = "STRING"
    value: str
