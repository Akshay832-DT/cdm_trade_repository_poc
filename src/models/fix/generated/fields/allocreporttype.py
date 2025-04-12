
from .base import FIXFieldBase
from .types import FIXInt

class AllocReportType(FIXFieldBase):
    """FIX AllocReportType field."""
    tag: str = "794"
    name: str = "AllocReportType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 3: SELLSIDE_CALCULATED_USING_PRELIMINARY
    # 4: SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY
    # 5: WAREHOUSE_RECAP
    # 8: REQUEST_TO_INTERMEDIARY
