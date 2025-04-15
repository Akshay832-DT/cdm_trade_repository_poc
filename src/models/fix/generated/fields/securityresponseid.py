"""
FIX SecurityResponseID field (tag 322).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SecurityResponseIDField(FIXFieldBase):
    """"""
    tag: str = "322"
    name: str = "SecurityResponseID"
    type: str = "STRING"
    value: str
