"""
FIX ExDestination field (tag 100).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ExDestinationField(FIXFieldBase):
    """"""
    tag: str = "100"
    name: str = "ExDestination"
    type: str = "EXCHANGE"
    value: str
