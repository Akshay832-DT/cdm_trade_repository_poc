
from .base import FIXFieldBase
from .types import FIXMultipleValueString

class ExecInst(FIXFieldBase):
    """FIX ExecInst field."""
    tag: str = "18"
    name: str = "ExecInst"
    type: str = "MULTIPLEVALUESTRING"
    value: FIXMultipleValueString

    # Enum values
    # 1: NOT_HELD
    # 2: WORK
    # 3: GO_ALONG
    # 4: OVER_THE_DAY
    # 5: HELD
    # 6: PARTICIPATE_DO_NOT_INITIATE
    # 7: STRICT_SCALE
    # 8: TRY_TO_SCALE
    # 9: STAY_ON_BID_SIDE
    # 0: STAY_ON_OFFER_SIDE
    # A: NO_CROSS
    # B: OK_TO_CROSS
    # C: CALL_FIRST
    # D: PERCENT_OF_VOLUME
    # E: DO_NOT_INCREASE
    # F: DO_NOT_REDUCE
    # G: ALL_OR_NONE
    # H: REINSTATE_ON_SYSTEM_FAILURE
    # I: INSTITUTIONS_ONLY
    # J: REINSTATE_ON_TRADING_HALT
    # K: CANCEL_ON_TRADING_HALT
    # L: LAST_PEG
    # M: MID_PRICE_PEG
    # N: NON_NEGOTIABLE
    # O: OPENING_PEG
    # P: MARKET_PEG
    # Q: CANCEL_ON_SYSTEM_FAILURE
    # R: PRIMARY_PEG
    # S: SUSPEND
    # U: CUSTOMER_DISPLAY_INSTRUCTION
    # V: NETTING
    # W: PEG_TO_VWAP
    # X: TRADE_ALONG
    # Y: TRY_TO_STOP
    # Z: CANCEL_IF_NOT_BEST
    # a: TRAILING_STOP_PEG
    # b: STRICT_LIMIT
    # c: IGNORE_PRICE_VALIDITY_CHECKS
    # d: PEG_TO_LIMIT_PRICE
    # e: WORK_TO_TARGET_STRATEGY
