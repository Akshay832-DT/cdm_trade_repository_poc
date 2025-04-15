"""
FIX NumTickets field (tag 395).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NumTicketsField(FIXFieldBase):
    """"""
    tag: str = "395"
    name: str = "NumTickets"
    type: str = "INT"
    value: int
