
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class SettlDate(FIXFieldBase):
    """FIX SettlDate field."""
    tag: str = "64"
    name: str = "SettlDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
