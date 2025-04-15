"""
FIX LocaleOfIssue field (tag 472).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class LocaleOfIssueField(FIXFieldBase):
    """"""
    tag: str = "472"
    name: str = "LocaleOfIssue"
    type: str = "STRING"
    value: str
