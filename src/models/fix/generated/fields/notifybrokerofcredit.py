"""
FIX NotifyBrokerOfCredit field (tag 208).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class NotifyBrokerOfCreditValues:
    """Enumerated values for NotifyBrokerOfCredit."""
    Y = "Y"  # YES
    N = "N"  # NO

class NotifyBrokerOfCreditField(FIXFieldBase):
    """"""
    tag: str = "208"
    name: str = "NotifyBrokerOfCredit"
    type: str = "BOOLEAN"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
