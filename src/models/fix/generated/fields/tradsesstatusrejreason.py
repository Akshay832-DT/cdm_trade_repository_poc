
from .base import FIXFieldBase
from .types import FIXInt

class TradSesStatusRejReason(FIXFieldBase):
    """FIX TradSesStatusRejReason field."""
    tag: str = "567"
    name: str = "TradSesStatusRejReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: UNKNOWN_OR_INVALID_TRADING_SESSION_ID
    # 99: OTHER
