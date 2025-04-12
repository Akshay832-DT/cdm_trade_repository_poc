
from .base import FIXFieldBase
from .types import FIXInt

class QuoteResponseLevel(FIXFieldBase):
    """FIX QuoteResponseLevel field."""
    tag: str = "301"
    name: str = "QuoteResponseLevel"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: NO_ACKNOWLEDGEMENT
    # 1: ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES
    # 2: ACKNOWLEDGE_EACH_QUOTE_MESSAGE
