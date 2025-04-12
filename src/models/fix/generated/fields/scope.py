
from .base import FIXFieldBase
from .types import FIXMultipleValueString

class Scope(FIXFieldBase):
    """FIX Scope field."""
    tag: str = "546"
    name: str = "Scope"
    type: str = "MULTIPLEVALUESTRING"
    value: FIXMultipleValueString

    # Enum values
    # 1: LOCAL_MARKET
    # 2: NATIONAL
    # 3: GLOBAL
