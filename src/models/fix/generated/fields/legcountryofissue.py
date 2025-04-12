
from .base import FIXFieldBase
from .types import FIXCountry

class LegCountryOfIssue(FIXFieldBase):
    """FIX LegCountryOfIssue field."""
    tag: str = "596"
    name: str = "LegCountryOfIssue"
    type: str = "COUNTRY"
    value: FIXCountry
