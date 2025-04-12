
from .base import FIXFieldBase
from .types import FIXMultipleValueString

class OrderRestrictions(FIXFieldBase):
    """FIX OrderRestrictions field."""
    tag: str = "529"
    name: str = "OrderRestrictions"
    type: str = "MULTIPLEVALUESTRING"
    value: FIXMultipleValueString

    # Enum values
    # 1: PROGRAM_TRADE
    # 2: INDEX_ARBITRAGE
    # 3: NON_INDEX_ARBITRAGE
    # 4: COMPETING_MARKET_MAKER
    # 5: ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_SECURITY
    # 6: ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_UNDERLYING
    # 7: FOREIGN_ENTITY
    # 8: EXTERNAL_MARKET_PARTICIPANT
    # 9: EXTERNAL_INTER_CONNECTED_MARKET_LINKAGE
    # A: RISKLESS_ARBITRAGE
