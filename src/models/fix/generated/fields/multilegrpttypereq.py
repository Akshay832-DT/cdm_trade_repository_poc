"""
FIX MultiLegRptTypeReq field (tag 563).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class MultiLegRptTypeReqValues:
    """Enumerated values for MultiLegRptTypeReq."""
    VALUE_0 = "0"  # REPORT_BY_MULITLEG_SECURITY_ONLY
    VALUE_1 = "1"  # REPORT_BY_MULTILEG_SECURITY_AND_INSTRUMENT_LEGS
    VALUE_2 = "2"  # REPORT_BY_INSTRUMENT_LEGS_ONLY

class MultiLegRptTypeReqField(FIXFieldBase):
    """"""
    tag: str = "563"
    name: str = "MultiLegRptTypeReq"
    type: str = "INT"
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
