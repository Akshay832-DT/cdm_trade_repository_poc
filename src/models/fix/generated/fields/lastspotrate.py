
from .base import FIXFieldBase
from .types import FIXPrice

class LastSpotRate(FIXFieldBase):
    """FIX LastSpotRate field."""
    tag: str = "194"
    name: str = "LastSpotRate"
    type: str = "PRICE"
    value: FIXPrice
