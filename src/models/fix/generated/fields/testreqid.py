"""
FIX TestReqID field (tag 112).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TestReqIDField(FIXFieldBase):
    """"""
    tag: str = "112"
    name: str = "TestReqID"
    type: str = "STRING"
    value: str
