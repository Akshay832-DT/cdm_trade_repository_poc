
from .base import FIXFieldBase
from .types import FIXLocalMktDate

class BasisFeatureDate(FIXFieldBase):
    """FIX BasisFeatureDate field."""
    tag: str = "259"
    name: str = "BasisFeatureDate"
    type: str = "LOCALMKTDATE"
    value: FIXLocalMktDate
