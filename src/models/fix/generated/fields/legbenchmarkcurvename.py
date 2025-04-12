
from .base import FIXFieldBase
from .types import FIXString

class LegBenchmarkCurveName(FIXFieldBase):
    """FIX LegBenchmarkCurveName field."""
    tag: str = "677"
    name: str = "LegBenchmarkCurveName"
    type: str = "STRING"
    value: FIXString
