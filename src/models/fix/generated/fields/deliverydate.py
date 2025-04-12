
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class DeliveryDate(FIXFieldBase):
    """FIX DeliveryDate field."""
    tag: str = "743"
    name: str = "DeliveryDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
