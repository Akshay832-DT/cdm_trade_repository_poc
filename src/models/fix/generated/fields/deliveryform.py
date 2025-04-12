
from .base import FIXFieldBase
from .types import FIXInt

class DeliveryForm(FIXFieldBase):
    """FIX DeliveryForm field."""
    tag: str = "668"
    name: str = "DeliveryForm"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: BOOK_ENTRY
    # 2: BEARER
