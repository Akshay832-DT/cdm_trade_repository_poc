
from .base import FIXFieldBase
from .types import FIXInt

class CollAsgnRespType(FIXFieldBase):
    """FIX CollAsgnRespType field."""
    tag: str = "905"
    name: str = "CollAsgnRespType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: RECEIVED
    # 1: ACCEPTED
    # 2: DECLINED
    # 3: REJECTED
