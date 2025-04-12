
from .base import FIXFieldBase
from .types import FIXInt

class TradSesStatus(FIXFieldBase):
    """FIX TradSesStatus field."""
    tag: str = "340"
    name: str = "TradSesStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: UNKNOWN
    # 1: HALTED
    # 2: OPEN
    # 3: CLOSED
    # 4: PRE_OPEN
    # 5: PRE_CLOSE
    # 6: REQUEST_REJECTED
