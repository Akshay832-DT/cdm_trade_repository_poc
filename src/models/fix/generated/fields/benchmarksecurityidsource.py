
from .base import FIXFieldBase
from .types import FIXString

class BenchmarkSecurityIDSource(FIXFieldBase):
    """FIX BenchmarkSecurityIDSource field."""
    tag: str = "761"
    name: str = "BenchmarkSecurityIDSource"
    type: str = "STRING"
    value: FIXString
