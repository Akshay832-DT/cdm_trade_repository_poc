"""
FIX AllowableOneSidednessValue field (tag 766).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllowableOneSidednessValueField(FIXFieldBase):
    """"""
    tag: str = "766"
    name: str = "AllowableOneSidednessValue"
    type: str = "AMT"
    value: float
