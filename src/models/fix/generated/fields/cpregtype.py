"""
FIX CPRegType field (tag 876).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CPRegTypeField(FIXFieldBase):
    """"""
    tag: str = "876"
    name: str = "CPRegType"
    type: str = "STRING"
    value: str
