
from .base import FIXFieldBase
from .types import FIXPrice

class MidPx(FIXFieldBase):
    """FIX MidPx field."""
    tag: str = "631"
    name: str = "MidPx"
    type: str = "PRICE"
    value: FIXPrice
