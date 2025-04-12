
from .base import FIXFieldBase
from .types import FIXInt

class SecurityRequestType(FIXFieldBase):
    """FIX SecurityRequestType field."""
    tag: str = "321"
    name: str = "SecurityRequestType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: REQUEST_SECURITY_IDENTITY_AND_SPECIFICATIONS
    # 1: REQUEST_SECURITY_IDENTITY_FOR_SPECIFICATIONS
    # 2: REQUEST_LIST_SECURITY_TYPES
    # 3: REQUEST_LIST_SECURITIES
