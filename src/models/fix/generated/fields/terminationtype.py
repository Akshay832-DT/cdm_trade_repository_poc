
from .base import FIXFieldBase
from .types import FIXInt

class TerminationType(FIXFieldBase):
    """FIX TerminationType field."""
    tag: str = "788"
    name: str = "TerminationType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: OVERNIGHT
    # 2: TERM
    # 3: FLEXIBLE
    # 4: OPEN
