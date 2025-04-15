"""
FIX CountryOfIssue field (tag 470).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CountryOfIssueField(FIXFieldBase):
    """"""
    tag: str = "470"
    name: str = "CountryOfIssue"
    type: str = "COUNTRY"
    value: str
