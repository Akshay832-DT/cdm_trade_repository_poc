
from .base import FIXFieldBase
from .types import FIXInt

class UserRequestType(FIXFieldBase):
    """FIX UserRequestType field."""
    tag: str = "924"
    name: str = "UserRequestType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: LOG_ON_USER
    # 2: LOG_OFF_USER
    # 3: CHANGE_PASSWORD_FOR_USER
    # 4: REQUEST_INDIVIDUAL_USER_STATUS
