
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class MaturityDate(FIXFieldBase):
    """FIX MaturityDate field."""
    tag: str = "541"
    name: str = "MaturityDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
