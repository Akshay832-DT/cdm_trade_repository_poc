
from .base import FIXFieldBase
from .types import FIXInt

class AllocNoOrdersType(FIXFieldBase):
    """FIX AllocNoOrdersType field."""
    tag: str = "857"
    name: str = "AllocNoOrdersType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: NOT_SPECIFIED
    # 1: EXPLICIT_LIST_PROVIDED
