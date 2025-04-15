"""
FIX NoMsgTypes field (tag 384).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NoMsgTypesField(FIXFieldBase):
    """"""
    tag: str = "384"
    name: str = "NoMsgTypes"
    type: str = "NUMINGROUP"
    value: int
