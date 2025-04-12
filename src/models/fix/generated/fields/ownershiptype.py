
from .base import FIXFieldBase
from .types import FIXChar

class OwnershipType(FIXFieldBase):
    """FIX OwnershipType field."""
    tag: str = "517"
    name: str = "OwnershipType"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # J: JOINT_INVESTORS
    # T: TENANTS_IN_COMMON
    # 2: JOINT_TRUSTEES
