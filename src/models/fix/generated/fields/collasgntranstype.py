
from .base import FIXFieldBase
from .types import FIXInt

class CollAsgnTransType(FIXFieldBase):
    """FIX CollAsgnTransType field."""
    tag: str = "903"
    name: str = "CollAsgnTransType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: NEW
    # 1: REPLACE
    # 2: CANCEL
    # 3: RELEASE
    # 4: REVERSE
