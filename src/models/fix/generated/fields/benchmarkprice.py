
from .base import FIXFieldBase
from .types import FIXPrice

class BenchmarkPrice(FIXFieldBase):
    """FIX BenchmarkPrice field."""
    tag: str = "662"
    name: str = "BenchmarkPrice"
    type: str = "PRICE"
    value: FIXPrice
