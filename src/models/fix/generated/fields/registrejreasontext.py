"""
FIX RegistRejReasonText field (tag 496).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RegistRejReasonTextField(FIXFieldBase):
    """"""
    tag: str = "496"
    name: str = "RegistRejReasonText"
    type: str = "STRING"
    value: str
