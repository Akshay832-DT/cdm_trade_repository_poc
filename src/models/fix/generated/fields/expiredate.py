
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class ExpireDate(FIXFieldBase):
    """FIX ExpireDate field."""
    tag: str = "432"
    name: str = "ExpireDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
