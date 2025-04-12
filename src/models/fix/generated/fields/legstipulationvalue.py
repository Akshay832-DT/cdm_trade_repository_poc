
from .base import FIXFieldBase
from .types import FIXString

class LegStipulationValue(FIXFieldBase):
    """FIX LegStipulationValue field."""
    tag: str = "689"
    name: str = "LegStipulationValue"
    type: str = "STRING"
    value: FIXString
