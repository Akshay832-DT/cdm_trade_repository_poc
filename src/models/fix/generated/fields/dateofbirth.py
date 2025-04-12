
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class DateOfBirth(FIXFieldBase):
    """FIX DateOfBirth field."""
    tag: str = "486"
    name: str = "DateOfBirth"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
