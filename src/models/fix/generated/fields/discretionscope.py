
from .base import FIXFieldBase
from .types import FIXInt

class DiscretionScope(FIXFieldBase):
    """FIX DiscretionScope field."""
    tag: str = "846"
    name: str = "DiscretionScope"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: LOCAL
    # 2: NATIONAL
    # 3: GLOBAL
    # 4: NATIONAL_EXCLUDING_LOCAL
