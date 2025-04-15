"""
FIX EncodedSubject field (tag 357).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedSubjectField(FIXFieldBase):
    """"""
    tag: str = "357"
    name: str = "EncodedSubject"
    type: str = "DATA"
    value: str
