
from .base import FIXFieldBase
from .types import FIXCountry

class CountryOfIssue(FIXFieldBase):
    """FIX CountryOfIssue field."""
    tag: str = "470"
    name: str = "CountryOfIssue"
    type: str = "COUNTRY"
    value: FIXCountry
