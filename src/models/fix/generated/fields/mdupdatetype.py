
from .base import FIXFieldBase
from .types import FIXInt

class MDUpdateType(FIXFieldBase):
    """FIX MDUpdateType field."""
    tag: str = "265"
    name: str = "MDUpdateType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: FULL_REFRESH
    # 1: INCREMENTAL_REFRESH
