"""
FIX AgreementDesc field (tag 913).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AgreementDescField(FIXFieldBase):
    """"""
    tag: str = "913"
    name: str = "AgreementDesc"
    type: str = "STRING"
    value: str
