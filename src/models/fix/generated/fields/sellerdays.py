
from .base import FIXFieldBase
from .types import FIXInt

class SellerDays(FIXFieldBase):
    """FIX SellerDays field."""
    tag: str = "287"
    name: str = "SellerDays"
    type: str = "INT"
    value: FIXInt
