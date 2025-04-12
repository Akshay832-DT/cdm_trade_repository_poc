
from .base import FIXFieldBase
from .types import FIXInt

class QtyType(FIXFieldBase):
    """FIX QtyType field."""
    tag: str = "854"
    name: str = "QtyType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: UNITS
    # 1: CONTRACTS
