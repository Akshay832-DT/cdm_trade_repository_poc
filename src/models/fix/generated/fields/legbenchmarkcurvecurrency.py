
from .base import FIXFieldBase
from .types import FIXCurrency

class LegBenchmarkCurveCurrency(FIXFieldBase):
    """FIX LegBenchmarkCurveCurrency field."""
    tag: str = "676"
    name: str = "LegBenchmarkCurveCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
