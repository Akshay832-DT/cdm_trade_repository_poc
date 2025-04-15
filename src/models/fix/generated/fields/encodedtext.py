"""
FIX EncodedText field (tag 355).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class EncodedTextField(FIXFieldBase):
    """"""
    tag: str = "355"
    name: str = "EncodedText"
    type: str = "DATA"
    value: str
