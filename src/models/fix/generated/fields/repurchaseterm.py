
from .base import FIXFieldBase
from .types import FIXInt

class RepurchaseTerm(FIXFieldBase):
    """FIX RepurchaseTerm field."""
    tag: str = "226"
    name: str = "RepurchaseTerm"
    type: str = "INT"
    value: FIXInt
