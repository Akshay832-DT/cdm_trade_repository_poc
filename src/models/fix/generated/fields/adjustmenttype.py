
from .base import FIXFieldBase
from .types import FIXInt

class AdjustmentType(FIXFieldBase):
    """FIX AdjustmentType field."""
    tag: str = "718"
    name: str = "AdjustmentType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: PROCESS_REQUEST_AS_MARGIN_DISPOSITION
    # 1: DELTA_PLUS
    # 2: DELTA_MINUS
    # 3: FINAL
