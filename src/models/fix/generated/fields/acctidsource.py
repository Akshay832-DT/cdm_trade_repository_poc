"""
FIX AcctIDSource field (tag 660).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AcctIDSourceValues:
    """Enumerated values for AcctIDSource."""
    VALUE_1 = "1"  # BIC
    VALUE_2 = "2"  # SID_CODE
    VALUE_3 = "3"  # TFM
    VALUE_4 = "4"  # OMGEO
    VALUE_5 = "5"  # DTCC_CODE
    VALUE_99 = "99"  # OTHER

class AcctIDSourceField(FIXFieldBase):
    """"""
    tag: str = "660"
    name: str = "AcctIDSource"
    type: str = "INT"
    value: Literal["1", "2", "3", "4", "5", "99"]

    # Helper methods for enum values
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
