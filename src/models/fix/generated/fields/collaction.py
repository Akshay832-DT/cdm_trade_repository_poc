
from .base import FIXFieldBase
from .types import FIXInt

class CollAction(FIXFieldBase):
    """FIX CollAction field."""
    tag: str = "944"
    name: str = "CollAction"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: RETAIN
    # 1: ADD
    # 2: REMOVE
