
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class UnderlyingMaturityDate(FIXFieldBase):
    """FIX UnderlyingMaturityDate field."""
    tag: str = "542"
    name: str = "UnderlyingMaturityDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
