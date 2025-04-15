"""
FIX SettlSessID field (tag 716).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SettlSessIDValues:
    """Enumerated values for SettlSessID."""
    ITD = "ITD"  # INTRADAY
    RTH = "RTH"  # REGULAR_TRADING_HOURS
    ETH = "ETH"  # ELECTRONIC_TRADING_HOURS

class SettlSessIDField(FIXFieldBase):
    """"""
    tag: str = "716"
    name: str = "SettlSessID"
    type: str = "STRING"
    value: Literal["ITD", "RTH", "ETH"]

    # Helper methods for enum values
    @property
    def is_itd(self) -> bool:
        return self.value == "ITD"
    @property
    def is_rth(self) -> bool:
        return self.value == "RTH"
    @property
    def is_eth(self) -> bool:
        return self.value == "ETH"
