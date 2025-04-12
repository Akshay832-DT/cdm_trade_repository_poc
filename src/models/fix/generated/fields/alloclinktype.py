
from .base import FIXFieldBase
from .types import FIXInt

class AllocLinkType(FIXFieldBase):
    """FIX AllocLinkType field."""
    tag: str = "197"
    name: str = "AllocLinkType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: FX_NETTING
    # 1: FX_SWAP
