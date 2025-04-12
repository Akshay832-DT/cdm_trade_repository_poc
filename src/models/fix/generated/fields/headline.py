
from .base import FIXFieldBase
from .types import FIXString

class Headline(FIXFieldBase):
    """FIX Headline field."""
    tag: str = "148"
    name: str = "Headline"
    type: str = "STRING"
    value: FIXString
