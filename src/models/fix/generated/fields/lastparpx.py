
from .base import FIXFieldBase
from .types import FIXPrice

class LastParPx(FIXFieldBase):
    """FIX LastParPx field."""
    tag: str = "669"
    name: str = "LastParPx"
    type: str = "PRICE"
    value: FIXPrice
