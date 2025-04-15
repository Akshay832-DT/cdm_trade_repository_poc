"""
FIX ResponseDestination field (tag 726).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ResponseDestinationField(FIXFieldBase):
    """"""
    tag: str = "726"
    name: str = "ResponseDestination"
    type: str = "STRING"
    value: str
