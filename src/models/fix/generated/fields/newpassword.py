"""
FIX NewPassword field (tag 925).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NewPasswordField(FIXFieldBase):
    """"""
    tag: str = "925"
    name: str = "NewPassword"
    type: str = "STRING"
    value: str
