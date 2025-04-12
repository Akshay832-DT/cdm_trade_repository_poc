
from .base import FIXFieldBase
from .types import FIXCurrency

class BenchmarkCurveCurrency(FIXFieldBase):
    """FIX BenchmarkCurveCurrency field."""
    tag: str = "220"
    name: str = "BenchmarkCurveCurrency"
    type: str = "CURRENCY"
    value: FIXCurrency
