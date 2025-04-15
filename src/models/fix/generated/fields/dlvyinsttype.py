"""
FIX DlvyInstType field (tag 787).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DlvyInstTypeValues:
    """Enumerated values for DlvyInstType."""
    S = "S"  # SECURITIES
    C = "C"  # CASH

class DlvyInstTypeField(FIXFieldBase):
    """"""
    tag: str = "787"
    name: str = "DlvyInstType"
    type: str = "CHAR"
    value: Literal["S", "C"]

    # Helper methods for enum values
    @property
    def is_s(self) -> bool:
        return self.value == "S"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
