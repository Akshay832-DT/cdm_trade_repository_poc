
from .base import FIXFieldBase
from .types import FIXString

class ExchangeRule(FIXFieldBase):
    """FIX ExchangeRule field."""
    tag: str = "825"
    name: str = "ExchangeRule"
    type: str = "STRING"
    value: FIXString
