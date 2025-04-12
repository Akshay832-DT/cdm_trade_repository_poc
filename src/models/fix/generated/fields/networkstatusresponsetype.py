
from .base import FIXFieldBase
from .types import FIXInt

class NetworkStatusResponseType(FIXFieldBase):
    """FIX NetworkStatusResponseType field."""
    tag: str = "937"
    name: str = "NetworkStatusResponseType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: FULL
    # 2: INCREMENTAL_UPDATE
