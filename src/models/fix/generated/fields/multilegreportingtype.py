
from .base import FIXFieldBase
from .types import FIXChar

class MultiLegReportingType(FIXFieldBase):
    """FIX MultiLegReportingType field."""
    tag: str = "442"
    name: str = "MultiLegReportingType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: SINGLE_SECURITY
    # 2: INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY
    # 3: MULTI_LEG_SECURITY
