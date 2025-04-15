"""
FIX FundRenewWaiv field (tag 497).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class FundRenewWaivValues:
    """Enumerated values for FundRenewWaiv."""
    Y = "Y"  # YES
    N = "N"  # NO

class FundRenewWaivField(FIXFieldBase):
    """"""
    tag: str = "497"
    name: str = "FundRenewWaiv"
    type: str = "CHAR"
    value: Literal["Y", "N"]

    # Helper methods for enum values
    @property
    def is_y(self) -> bool:
        return self.value == "Y"
    @property
    def is_n(self) -> bool:
        return self.value == "N"
