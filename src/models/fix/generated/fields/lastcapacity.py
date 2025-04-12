
from .base import FIXFieldBase
from .types import FIXChar

class LastCapacity(FIXFieldBase):
    """FIX LastCapacity field."""
    tag: str = "29"
    name: str = "LastCapacity"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # 1: AGENT
    # 2: CROSS_AS_AGENT
    # 3: CROSS_AS_PRINCIPAL
    # 4: PRINCIPAL
