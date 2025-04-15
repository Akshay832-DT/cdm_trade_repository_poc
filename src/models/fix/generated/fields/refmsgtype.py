"""
FIX RefMsgType field (tag 372).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RefMsgTypeField(FIXFieldBase):
    """"""
    tag: str = "372"
    name: str = "RefMsgType"
    type: str = "STRING"
    value: str
