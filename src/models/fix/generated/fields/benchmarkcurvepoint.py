
from .base import FIXFieldBase
from .types import FIXString

class BenchmarkCurvePoint(FIXFieldBase):
    """FIX BenchmarkCurvePoint field."""
    tag: str = "222"
    name: str = "BenchmarkCurvePoint"
    type: str = "STRING"
    value: FIXString
