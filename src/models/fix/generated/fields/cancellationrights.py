
from .base import FIXFieldBase
from .types import FIXChar

class CancellationRights(FIXFieldBase):
    """FIX CancellationRights field."""
    tag: str = "480"
    name: str = "CancellationRights"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # Y: YES
    # N: NO_EXECUTION_ONLY
    # M: NO_WAIVER_AGREEMENT
    # O: NO_INSTITUTIONAL
