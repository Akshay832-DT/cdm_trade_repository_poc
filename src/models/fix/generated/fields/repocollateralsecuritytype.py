"""
FIX RepoCollateralSecurityType field (tag 239).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class RepoCollateralSecurityTypeField(FIXFieldBase):
    """"""
    tag: str = "239"
    name: str = "RepoCollateralSecurityType"
    type: str = "STRING"
    value: str
