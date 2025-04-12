
from .base import FIXFieldBase
from .types import FIXInt

class QuoteRequestType(FIXFieldBase):
    """FIX QuoteRequestType field."""
    tag: str = "303"
    name: str = "QuoteRequestType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: MANUAL
    # 2: AUTOMATIC
