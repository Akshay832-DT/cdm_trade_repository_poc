
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class ExDate(FIXFieldBase):
    """FIX ExDate field."""
    tag: str = "230"
    name: str = "ExDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
