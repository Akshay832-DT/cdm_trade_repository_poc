
from .base import FIXFieldBase
from .types import FIXInt

class SideValueInd(FIXFieldBase):
    """FIX SideValueInd field."""
    tag: str = "401"
    name: str = "SideValueInd"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: SIDE_VALUE1
    # 2: SIDE_VALUE2
