
from .base import FIXFieldBase
from .types import FIXInt

class LastLiquidityInd(FIXFieldBase):
    """FIX LastLiquidityInd field."""
    tag: str = "851"
    name: str = "LastLiquidityInd"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: ADDED_LIQUIDITY
    # 2: REMOVED_LIQUIDITY
    # 3: LIQUIDITY_ROUTED_OUT
