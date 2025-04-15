"""
FIX Designation field (tag 494).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DesignationField(FIXFieldBase):
    """"""
    tag: str = "494"
    name: str = "Designation"
    type: str = "STRING"
    value: str
