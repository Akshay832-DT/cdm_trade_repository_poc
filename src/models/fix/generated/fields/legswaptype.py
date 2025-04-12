
from .base import FIXFieldBase
from .types import FIXInt

class LegSwapType(FIXFieldBase):
    """FIX LegSwapType field."""
    tag: str = "690"
    name: str = "LegSwapType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: PAR_FOR_PAR
    # 2: MODIFIED_DURATION
    # 4: RISK
    # 5: PROCEEDS
