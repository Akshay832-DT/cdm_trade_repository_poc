"""
FIX AllocReportType field (tag 794).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class AllocReportTypeValues:
    """Enumerated values for AllocReportType."""
    VALUE_3 = "3"  # SELLSIDE_CALCULATED_USING_PRELIMINARY
    VALUE_4 = "4"  # SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY
    VALUE_5 = "5"  # WAREHOUSE_RECAP
    VALUE_8 = "8"  # REQUEST_TO_INTERMEDIARY

class AllocReportTypeField(FIXFieldBase):
    """"""
    tag: str = "794"
    name: str = "AllocReportType"
    type: str = "INT"
    value: Literal["3", "4", "5", "8"]

    # Helper methods for enum values
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
    def is_value_8(self) -> bool:
        return self.value == "8"
