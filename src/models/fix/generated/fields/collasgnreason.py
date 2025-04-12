
from .base import FIXFieldBase
from .types import FIXInt

class CollAsgnReason(FIXFieldBase):
    """FIX CollAsgnReason field."""
    tag: str = "895"
    name: str = "CollAsgnReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: INITIAL
    # 1: SCHEDULED
    # 2: TIME_WARNING
    # 3: MARGIN_DEFICIENCY
    # 4: MARGIN_EXCESS
    # 5: FORWARD_COLLATERAL_DEMAND
    # 6: EVENT_OF_DEFAULT
    # 7: ADVERSE_TAX_EVENT
