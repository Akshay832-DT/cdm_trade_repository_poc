
from .base import FIXFieldBase
from .types import FIXInt

class ConfirmType(FIXFieldBase):
    """FIX ConfirmType field."""
    tag: str = "773"
    name: str = "ConfirmType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: STATUS
    # 2: CONFIRMATION
    # 3: CONFIRMATION_REQUEST_REJECTED
