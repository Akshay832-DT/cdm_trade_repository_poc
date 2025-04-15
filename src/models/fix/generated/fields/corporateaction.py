"""
FIX CorporateAction field (tag 292).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CorporateActionValues:
    """Enumerated values for CorporateAction."""
    A = "A"  # EX_DIVIDEND
    B = "B"  # EX_DISTRIBUTION
    C = "C"  # EX_RIGHTS
    D = "D"  # NEW
    E = "E"  # EX_INTEREST

class CorporateActionField(FIXFieldBase):
    """"""
    tag: str = "292"
    name: str = "CorporateAction"
    type: str = "MULTIPLEVALUESTRING"
    value: List[str]

    # Helper methods for enum values
    @property
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_b(self) -> bool:
        return self.value == "B"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
    @property
    def is_d(self) -> bool:
        return self.value == "D"
    @property
    def is_e(self) -> bool:
        return self.value == "E"
