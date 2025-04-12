
from .base import FIXFieldBase
from .types import FIXString

class IOIQty(FIXFieldBase):
    """FIX IOIQty field."""
    tag: str = "27"
    name: str = "IOIQty"
    type: str = "STRING"
    value: FIXString

    # Enum values
    # S: SMALL
    # M: MEDIUM
    # L: LARGE
