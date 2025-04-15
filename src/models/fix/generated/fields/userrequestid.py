"""
FIX UserRequestID field (tag 923).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class UserRequestIDField(FIXFieldBase):
    """"""
    tag: str = "923"
    name: str = "UserRequestID"
    type: str = "STRING"
    value: str
