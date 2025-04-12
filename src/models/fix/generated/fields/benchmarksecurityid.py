
from .base import FIXFieldBase
from .types import FIXString

class BenchmarkSecurityID(FIXFieldBase):
    """FIX BenchmarkSecurityID field."""
    tag: str = "699"
    name: str = "BenchmarkSecurityID"
    type: str = "STRING"
    value: FIXString
