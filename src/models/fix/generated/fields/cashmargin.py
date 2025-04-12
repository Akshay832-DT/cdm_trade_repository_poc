
from .base import FIXFieldBase
from .types import FIXChar

class CashMargin(FIXFieldBase):
    """FIX CashMargin field."""
    tag: str = "544"
    name: str = "CashMargin"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: CASH
    # 2: MARGIN_OPEN
    # 3: MARGIN_CLOSE
