"""
FIX DeliveryType field (tag 919).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class DeliveryTypeValues:
    """Enumerated values for DeliveryType."""
    VALUE_0 = "0"  # VERSUS_PAYMENT
    VALUE_1 = "1"  # FREE
    VALUE_2 = "2"  # TRI_PARTY
    VALUE_3 = "3"  # HOLD_IN_CUSTODY

class DeliveryTypeField(FIXFieldBase):
    """"""
    tag: str = "919"
    name: str = "DeliveryType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3"]

    # Helper methods for enum values
    @property
    def is_value_0(self) -> bool:
        return self.value == "0"
    @property
    def is_value_1(self) -> bool:
        return self.value == "1"
    @property
    def is_value_2(self) -> bool:
        return self.value == "2"
    @property
    def is_value_3(self) -> bool:
        return self.value == "3"
