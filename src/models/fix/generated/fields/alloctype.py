
from .base import FIXFieldBase
from .types import FIXInt

class AllocType(FIXFieldBase):
    """FIX AllocType field."""
    tag: str = "626"
    name: str = "AllocType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: CALCULATED
    # 2: PRELIMINARY
    # 5: READY_TO_BOOK
    # 7: WAREHOUSE_INSTRUCTION
    # 8: REQUEST_TO_INTERMEDIARY
