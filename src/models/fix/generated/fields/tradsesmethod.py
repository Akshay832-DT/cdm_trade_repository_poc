
from .base import FIXFieldBase
from .types import FIXInt

class TradSesMethod(FIXFieldBase):
    """FIX TradSesMethod field."""
    tag: str = "338"
    name: str = "TradSesMethod"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: ELECTRONIC
    # 2: OPEN_OUTCRY
    # 3: TWO_PARTY
