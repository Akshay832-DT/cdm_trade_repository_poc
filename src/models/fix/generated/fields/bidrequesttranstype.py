"""
FIX BidRequestTransType field (tag 374).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidRequestTransTypeValues:
    """Enumerated values for BidRequestTransType."""
    N = "N"  # NEW
    C = "C"  # CANCEL

class BidRequestTransTypeField(FIXFieldBase):
    """"""
    tag: str = "374"
    name: str = "BidRequestTransType"
    type: str = "CHAR"
    value: Literal["N", "C"]

    # Helper methods for enum values
    @property
    def is_n(self) -> bool:
        return self.value == "N"
    @property
    def is_c(self) -> bool:
        return self.value == "C"
