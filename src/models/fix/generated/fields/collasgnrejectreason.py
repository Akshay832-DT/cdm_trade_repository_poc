
from .base import FIXFieldBase
from .types import FIXInt

class CollAsgnRejectReason(FIXFieldBase):
    """FIX CollAsgnRejectReason field."""
    tag: str = "906"
    name: str = "CollAsgnRejectReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: UNKNOWN_DEAL
    # 1: UNKNOWN_OR_INVALID_INSTRUMENT
    # 2: UNAUTHORIZED_TRANSACTION
    # 3: INSUFFICIENT_COLLATERAL
    # 4: INVALID_TYPE_OF_COLLATERAL
    # 5: EXCESSIVE_SUBSTITUTION
    # 99: OTHER
