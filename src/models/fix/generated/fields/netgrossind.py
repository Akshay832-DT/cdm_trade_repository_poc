"""
FIX NetGrossInd field (tag 430).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NetGrossIndValues:
    """Enumerated values for NetGrossInd."""
    VALUE_1 = "1"  # NET
    VALUE_2 = "2"  # GROSS

class NetGrossIndField(FIXFieldBase):
    """"""
    tag: str = "430"
    name: str = "NetGrossInd"
    type: str = "INT"
    value: Literal["1", "2"]

    # Helper methods for enum values
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
