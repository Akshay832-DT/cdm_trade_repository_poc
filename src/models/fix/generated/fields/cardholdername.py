
from .base import FIXFieldBase
from .types import FIXString

class CardHolderName(FIXFieldBase):
    """FIX CardHolderName field."""
    tag: str = "488"
    name: str = "CardHolderName"
    type: str = "STRING"
    value: FIXString
