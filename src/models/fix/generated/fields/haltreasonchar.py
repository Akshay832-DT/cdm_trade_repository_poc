"""
FIX HaltReasonChar field (tag 327).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class HaltReasonCharValues:
    """Enumerated values for HaltReasonChar."""
    I = "I"  # ORDER_IMBALANCE
    X = "X"  # EQUIPMENT_CHANGEOVER
    P = "P"  # NEWS_PENDING
    D = "D"  # NEWS_DISSEMINATION
    E = "E"  # ORDER_INFLUX
    M = "M"  # ADDITIONAL_INFORMATION

class HaltReasonCharField(FIXFieldBase):
    """"""
    tag: str = "327"
    name: str = "HaltReasonChar"
    type: str = "CHAR"
    value: Literal["I", "X", "P", "D", "E", "M"]

    # Helper methods for enum values
    @property
    def is_i(self) -> bool:
        return self.value == "I"
    @property
    def is_x(self) -> bool:
        return self.value == "X"
    @property
    def is_p(self) -> bool:
        return self.value == "P"
    @property
    def is_d(self) -> bool:
        return self.value == "D"
    @property
    def is_e(self) -> bool:
        return self.value == "E"
    @property
    def is_m(self) -> bool:
        return self.value == "M"
