
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class LegMaturityDate(FIXFieldBase):
    """FIX LegMaturityDate field."""
    tag: str = "611"
    name: str = "LegMaturityDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
