
from .base import FIXFieldBase
from .types import FIXString

class StipulationValue(FIXFieldBase):
    """FIX StipulationValue field."""
    tag: str = "234"
    name: str = "StipulationValue"
    type: str = "STRING"
    value: FIXString
