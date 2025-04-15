"""
FIX SubscriptionRequestType field (tag 263).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SubscriptionRequestTypeValues:
    """Enumerated values for SubscriptionRequestType."""
    VALUE_0 = "0"  # SNAPSHOT
    VALUE_1 = "1"  # SNAPSHOT_AND_UPDATES
    VALUE_2 = "2"  # DISABLE_PREVIOUS_SNAPSHOT

class SubscriptionRequestTypeField(FIXFieldBase):
    """"""
    tag: str = "263"
    name: str = "SubscriptionRequestType"
    type: str = "CHAR"
    value: Literal["0", "1", "2"]

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
