
from .base import FIXFieldBase
from .types import FIXInt

class TradSesMode(FIXFieldBase):
    """FIX TradSesMode field."""
    tag: str = "339"
    name: str = "TradSesMode"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: TESTING
    # 2: SIMULATED
    # 3: PRODUCTION
