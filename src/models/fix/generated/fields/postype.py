"""
FIX PosType field (tag 703).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class PosTypeValues:
    """Enumerated values for PosType."""
    TQ = "TQ"  # TRANSACTION_QUANTITY
    IAS = "IAS"  # INTRA_SPREAD_QTY
    IES = "IES"  # INTER_SPREAD_QTY
    FIN = "FIN"  # END_OF_DAY_QTY
    SOD = "SOD"  # START_OF_DAY_QTY
    EX = "EX"  # OPTION_EXERCISE_QTY
    AS = "AS"  # OPTION_ASSIGNMENT
    TX = "TX"  # TRANSACTION_FROM_EXERCISE
    TA = "TA"  # TRANSACTION_FROM_ASSIGNMENT
    PIT = "PIT"  # PIT_TRADE_QTY
    TRF = "TRF"  # TRANSFER_TRADE_QTY
    ETR = "ETR"  # ELECTRONIC_TRADE_QTY
    ALC = "ALC"  # ALLOCATION_TRADE_QTY
    PA = "PA"  # ADJUSTMENT_QTY
    ASF = "ASF"  # AS_OF_TRADE_QTY
    DLV = "DLV"  # DELIVERY_QTY
    TOT = "TOT"  # TOTAL_TRANSACTION_QTY
    XM = "XM"  # CROSS_MARGIN_QTY
    SPL = "SPL"  # INTEGRAL_SPLIT

class PosTypeField(FIXFieldBase):
    """"""
    tag: str = "703"
    name: str = "PosType"
    type: str = "STRING"
    value: Literal["TQ", "IAS", "IES", "FIN", "SOD", "EX", "AS", "TX", "TA", "PIT", "TRF", "ETR", "ALC", "PA", "ASF", "DLV", "TOT", "XM", "SPL"]

    # Helper methods for enum values
    @property
    def is_tq(self) -> bool:
        return self.value == "TQ"
    @property
    def is_ias(self) -> bool:
        return self.value == "IAS"
    @property
    def is_ies(self) -> bool:
        return self.value == "IES"
    @property
    def is_fin(self) -> bool:
        return self.value == "FIN"
    @property
    def is_sod(self) -> bool:
        return self.value == "SOD"
    @property
    def is_ex(self) -> bool:
        return self.value == "EX"
    @property
    def is_as(self) -> bool:
        return self.value == "AS"
    @property
    def is_tx(self) -> bool:
        return self.value == "TX"
    @property
    def is_ta(self) -> bool:
        return self.value == "TA"
    @property
    def is_pit(self) -> bool:
        return self.value == "PIT"
    @property
    def is_trf(self) -> bool:
        return self.value == "TRF"
    @property
    def is_etr(self) -> bool:
        return self.value == "ETR"
    @property
    def is_alc(self) -> bool:
        return self.value == "ALC"
    @property
    def is_pa(self) -> bool:
        return self.value == "PA"
    @property
    def is_asf(self) -> bool:
        return self.value == "ASF"
    @property
    def is_dlv(self) -> bool:
        return self.value == "DLV"
    @property
    def is_tot(self) -> bool:
        return self.value == "TOT"
    @property
    def is_xm(self) -> bool:
        return self.value == "XM"
    @property
    def is_spl(self) -> bool:
        return self.value == "SPL"
