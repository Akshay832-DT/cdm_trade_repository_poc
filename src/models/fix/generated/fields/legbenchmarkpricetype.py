
from .base import FIXFieldBase
from .types import FIXInt

class LegBenchmarkPriceType(FIXFieldBase):
    """FIX LegBenchmarkPriceType field."""
    tag: str = "680"
    name: str = "LegBenchmarkPriceType"
    type: str = "INT"
    value: FIXInt
