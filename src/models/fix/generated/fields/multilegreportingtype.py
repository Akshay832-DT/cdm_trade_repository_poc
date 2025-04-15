"""
FIX MultiLegReportingType field (tag 442).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MultiLegReportingTypeValues:
    """Enumerated values for MultiLegReportingType."""
    VALUE_1 = "1"  # SINGLE_SECURITY
    VALUE_2 = "2"  # INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY
    VALUE_3 = "3"  # MULTI_LEG_SECURITY

class MultiLegReportingTypeField(FIXFieldBase):
    """"""
    tag: str = "442"
    name: str = "MultiLegReportingType"
    type: str = "CHAR"
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
