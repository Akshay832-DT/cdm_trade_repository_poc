
from .base import FIXFieldBase
from .types import FIXInt

class UserStatus(FIXFieldBase):
    """FIX UserStatus field."""
    tag: str = "926"
    name: str = "UserStatus"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: LOGGED_IN
    # 2: NOT_LOGGED_IN
    # 3: USER_NOT_RECOGNISED
    # 4: PASSWORD_INCORRECT
    # 5: PASSWORD_CHANGED
    # 6: OTHER
