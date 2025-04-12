
from .base import FIXFieldBase
from .types import FIXString

class LegBenchmarkCurvePoint(FIXFieldBase):
    """FIX LegBenchmarkCurvePoint field."""
    tag: str = "678"
    name: str = "LegBenchmarkCurvePoint"
    type: str = "STRING"
    value: FIXString
