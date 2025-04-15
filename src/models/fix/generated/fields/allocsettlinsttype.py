"""
FIX AllocSettlInstType field (tag 780).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocSettlInstTypeValues:
    """Enumerated values for AllocSettlInstType."""
    VALUE_0 = "0"  # USE_DEFAULT_INSTRUCTIONS
    VALUE_1 = "1"  # DERIVE_FROM_PARAMETERS_PROVIDED
    VALUE_2 = "2"  # FULL_DETAILS_PROVIDED
    VALUE_3 = "3"  # SSIDBI_DS_PROVIDED
    VALUE_4 = "4"  # PHONE_FOR_INSTRUCTIONS

class AllocSettlInstTypeField(FIXFieldBase):
    """"""
    tag: str = "780"
    name: str = "AllocSettlInstType"
    type: str = "INT"
    value: Literal["0", "1", "2", "3", "4"]

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
