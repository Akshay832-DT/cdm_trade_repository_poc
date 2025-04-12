
from .base import FIXFieldBase
from .types import FIXInt

class IncTaxInd(FIXFieldBase):
    """FIX IncTaxInd field."""
    tag: str = "416"
    name: str = "IncTaxInd"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: NET
    # 2: GROSS
