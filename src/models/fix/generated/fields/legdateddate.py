
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class LegDatedDate(FIXFieldBase):
    """FIX LegDatedDate field."""
    tag: str = "739"
    name: str = "LegDatedDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
