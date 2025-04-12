
from .base import FIXFieldBase
from .types import FIXInt

class SideMultiLegReportingType(FIXFieldBase):
    """FIX SideMultiLegReportingType field."""
    tag: str = "752"
    name: str = "SideMultiLegReportingType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: SINGLE_SECURITY
    # 2: INDIVIDUAL_LEG_OF_A_MULTILEG_SECURITY
    # 3: MULTILEG_SECURITY
