"""
FIX BidTradeType field (tag 418).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BidTradeTypeValues:
    """Enumerated values for BidTradeType."""
    R = "R"  # RISK_TRADE
    G = "G"  # VWAP_GUARANTEE
    A = "A"  # AGENCY
    J = "J"  # GUARANTEED_CLOSE

class BidTradeTypeField(FIXFieldBase):
    """"""
    tag: str = "418"
    name: str = "BidTradeType"
    type: str = "CHAR"
    value: Literal["R", "G", "A", "J"]

    # Helper methods for enum values
    @property
    def is_r(self) -> bool:
        return self.value == "R"
    @property
    def is_g(self) -> bool:
        return self.value == "G"
    @property
    def is_a(self) -> bool:
        return self.value == "A"
    @property
    def is_j(self) -> bool:
        return self.value == "J"
