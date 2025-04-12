
from .base import FIXFieldBase
from .types import FIXInt

class ExpirationCycle(FIXFieldBase):
    """FIX ExpirationCycle field."""
    tag: str = "827"
    name: str = "ExpirationCycle"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: EXPIRE_ON_TRADING_SESSION_CLOSE
    # 1: EXPIRE_ON_TRADING_SESSION_OPEN
