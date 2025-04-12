
from .base import FIXFieldBase
from .types import FIXPrice

class LegBenchmarkPrice(FIXFieldBase):
    """FIX LegBenchmarkPrice field."""
    tag: str = "679"
    name: str = "LegBenchmarkPrice"
    type: str = "PRICE"
    value: FIXPrice
