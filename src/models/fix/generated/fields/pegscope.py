
from .base import FIXFieldBase
from .types import FIXInt

class PegScope(FIXFieldBase):
    """FIX PegScope field."""
    tag: str = "840"
    name: str = "PegScope"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: LOCAL
    # 2: NATIONAL
    # 3: GLOBAL
    # 4: NATIONAL_EXCLUDING_LOCAL
