"""
FIX CollAsgnReason field (tag 895).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class CollAsgnReasonValues:
    """Enumerated values for CollAsgnReason."""
    VALUE_0 = "0"  # INITIAL
    VALUE_1 = "1"  # SCHEDULED
    VALUE_2 = "2"  # TIME_WARNING
    VALUE_3 = "3"  # MARGIN_DEFICIENCY
    VALUE_4 = "4"  # MARGIN_EXCESS
    VALUE_5 = "5"  # FORWARD_COLLATERAL_DEMAND
    VALUE_6 = "6"  # EVENT_OF_DEFAULT
    VALUE_7 = "7"  # ADVERSE_TAX_EVENT

class CollAsgnReasonField(FIXFieldBase):
    """"""
    tag: str = "895"
    name: str = "CollAsgnReason"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4", "5", "6", "7"]

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
    def is_value_6(self) -> bool:
        return self.value == "6"
    @property
    def is_value_7(self) -> bool:
        return self.value == "7"
