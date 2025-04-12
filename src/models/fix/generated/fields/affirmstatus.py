
from .base import FIXFieldBase
from .types import FIXInt

class AffirmStatus(FIXFieldBase):
    """FIX AffirmStatus field."""
    tag: str = "940"
    name: str = "AffirmStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: RECEIVED
    # 2: CONFIRM_REJECTED
    # 3: AFFIRMED
