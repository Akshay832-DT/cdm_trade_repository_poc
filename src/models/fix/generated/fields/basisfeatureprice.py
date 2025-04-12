
from .base import FIXFieldBase
from .types import FIXPrice

class BasisFeaturePrice(FIXFieldBase):
    """FIX BasisFeaturePrice field."""
    tag: str = "260"
    name: str = "BasisFeaturePrice"
    type: str = "PRICE"
    value: FIXPrice
