"""
FIX Country field (tag 421).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CountryField(FIXFieldBase):
    """"""
    tag: str = "421"
    name: str = "Country"
    type: str = "COUNTRY"
    value: str
