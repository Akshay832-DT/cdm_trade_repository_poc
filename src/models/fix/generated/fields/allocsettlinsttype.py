
from .base import FIXFieldBase
from .types import FIXInt

class AllocSettlInstType(FIXFieldBase):
    """FIX AllocSettlInstType field."""
    tag: str = "780"
    name: str = "AllocSettlInstType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: USE_DEFAULT_INSTRUCTIONS
    # 1: DERIVE_FROM_PARAMETERS_PROVIDED
    # 2: FULL_DETAILS_PROVIDED
    # 3: SSIDBI_DS_PROVIDED
    # 4: PHONE_FOR_INSTRUCTIONS
