
from .base import FIXFieldBase
from .types import FIXInt

class QuoteType(FIXFieldBase):
    """FIX QuoteType field."""
    tag: str = "537"
    name: str = "QuoteType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: INDICATIVE
    # 1: TRADEABLE
    # 2: RESTRICTED_TRADEABLE
    # 3: COUNTER
