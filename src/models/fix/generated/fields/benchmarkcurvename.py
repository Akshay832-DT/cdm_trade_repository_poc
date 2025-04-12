
from .base import FIXFieldBase
from .types import FIXString

class BenchmarkCurveName(FIXFieldBase):
    """FIX BenchmarkCurveName field."""
    tag: str = "221"
    name: str = "BenchmarkCurveName"
    type: str = "STRING"
    value: FIXString
