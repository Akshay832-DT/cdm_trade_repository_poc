
from .base import FIXFieldBase
from .types import FIXInt

class ConfirmTransType(FIXFieldBase):
    """FIX ConfirmTransType field."""
    tag: str = "666"
    name: str = "ConfirmTransType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: NEW
    # 1: REPLACE
    # 2: CANCEL
