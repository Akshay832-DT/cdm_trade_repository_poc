"""
FIX Signature field (tag 89).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SignatureField(FIXFieldBase):
    """"""
    tag: str = "89"
    name: str = "Signature"
    type: str = "DATA"
    value: str
