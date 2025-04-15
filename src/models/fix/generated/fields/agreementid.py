"""
FIX AgreementID field (tag 914).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AgreementIDField(FIXFieldBase):
    """"""
    tag: str = "914"
    name: str = "AgreementID"
    type: str = "STRING"
    value: str
