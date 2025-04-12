
from .base import FIXFieldBase
from .types import FIXInt

class NetworkRequestType(FIXFieldBase):
    """FIX NetworkRequestType field."""
    tag: str = "935"
    name: str = "NetworkRequestType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: SNAPSHOT
    # 2: SUBSCRIBE
    # 4: STOP_SUBSCRIBING
    # 8: LEVEL_OF_DETAIL
