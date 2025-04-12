
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class SettlDate2(FIXFieldBase):
    """FIX SettlDate2 field."""
    tag: str = "193"
    name: str = "SettlDate2"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
