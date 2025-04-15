"""
FIX TradedFlatSwitch field (tag 258).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class TradedFlatSwitchValues:
    """Enumerated values for TradedFlatSwitch."""
    Y = "Y"  # YES
    N = "N"  # NO

class TradedFlatSwitchField(FIXFieldBase):
    """"""
    tag: str = "258"
    name: str = "TradedFlatSwitch"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
