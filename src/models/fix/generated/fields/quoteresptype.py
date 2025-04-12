
from .base import FIXFieldBase
from .types import FIXInt

class QuoteRespType(FIXFieldBase):
    """FIX QuoteRespType field."""
    tag: str = "694"
    name: str = "QuoteRespType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: HIT
    # 2: COUNTER
    # 3: EXPIRED
    # 4: COVER
    # 5: DONE_AWAY
    # 6: PASS
