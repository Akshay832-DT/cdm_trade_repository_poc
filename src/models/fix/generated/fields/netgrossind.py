
from .base import FIXFieldBase
from .types import FIXInt

class NetGrossInd(FIXFieldBase):
    """FIX NetGrossInd field."""
    tag: str = "430"
    name: str = "NetGrossInd"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: NET
    # 2: GROSS
