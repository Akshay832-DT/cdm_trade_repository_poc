"""
FIX AgreementDate field (tag 915).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AgreementDateField(FIXFieldBase):
    """"""
    tag: str = "915"
    name: str = "AgreementDate"
    type: str = "LOCALMKTDATE"
    value: date
