"""
FIX CollAsgnRejectReason field (tag 906).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollAsgnRejectReasonValues:
    """Enumerated values for CollAsgnRejectReason."""
    VALUE_0 = "0"  # UNKNOWN_DEAL
    VALUE_1 = "1"  # UNKNOWN_OR_INVALID_INSTRUMENT
    VALUE_2 = "2"  # UNAUTHORIZED_TRANSACTION
    VALUE_3 = "3"  # INSUFFICIENT_COLLATERAL
    VALUE_4 = "4"  # INVALID_TYPE_OF_COLLATERAL
    VALUE_5 = "5"  # EXCESSIVE_SUBSTITUTION
    VALUE_99 = "99"  # OTHER

class CollAsgnRejectReasonField(FIXFieldBase):
    """"""
    tag: str = "906"
    name: str = "CollAsgnRejectReason"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "99"]

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
    @property
    def is_value_4(self) -> bool:
        return self.value == "4"
    @property
    def is_value_5(self) -> bool:
        return self.value == "5"
    @property
    def is_value_99(self) -> bool:
        return self.value == "99"
