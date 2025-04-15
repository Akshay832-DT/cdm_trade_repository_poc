"""
FIX SideMultiLegReportingType field (tag 752).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class SideMultiLegReportingTypeValues:
    """Enumerated values for SideMultiLegReportingType."""
    VALUE_1 = "1"  # SINGLE_SECURITY
    VALUE_2 = "2"  # INDIVIDUAL_LEG_OF_A_MULTILEG_SECURITY
    VALUE_3 = "3"  # MULTILEG_SECURITY

class SideMultiLegReportingTypeField(FIXFieldBase):
    """"""
    tag: str = "752"
    name: str = "SideMultiLegReportingType"
    type: str = "INT"
    value: Literal["1", "2", "3"]

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
