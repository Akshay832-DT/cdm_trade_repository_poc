"""
FIX Subject field (tag 147).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SubjectField(FIXFieldBase):
    """"""
    tag: str = "147"
    name: str = "Subject"
    type: str = "STRING"
    value: str
