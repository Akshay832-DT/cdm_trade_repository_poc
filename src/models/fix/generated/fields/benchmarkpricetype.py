
from .base import FIXFieldBase
from .types import FIXInt

class BenchmarkPriceType(FIXFieldBase):
    """FIX BenchmarkPriceType field."""
    tag: str = "663"
    name: str = "BenchmarkPriceType"
    type: str = "INT"
    value: FIXInt
