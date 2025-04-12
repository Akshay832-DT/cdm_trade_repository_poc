
from .base import FIXFieldBase
from .types import FIXString

class LegStipulationType(FIXFieldBase):
    """FIX LegStipulationType field."""
    tag: str = "688"
    name: str = "LegStipulationType"
    type: str = "STRING"
    value: FIXString
