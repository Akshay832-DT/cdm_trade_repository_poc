
from .base import FIXFieldBase
from .types import FIXPrice

class Price2(FIXFieldBase):
    """FIX Price2 field."""
    tag: str = "640"
    name: str = "Price2"
    type: str = "PRICE"
    value: FIXPrice
