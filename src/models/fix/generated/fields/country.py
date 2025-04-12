
from .base import FIXFieldBase
from .types import FIXCountry

class Country(FIXFieldBase):
    """FIX Country field."""
    tag: str = "421"
    name: str = "Country"
    type: str = "COUNTRY"
    value: FIXCountry
