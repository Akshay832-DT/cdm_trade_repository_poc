"""
FIX SignatureLength field (tag 93).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SignatureLengthField(FIXFieldBase):
    """"""
    tag: str = "93"
    name: str = "SignatureLength"
    type: str = "LENGTH"
    value: int
